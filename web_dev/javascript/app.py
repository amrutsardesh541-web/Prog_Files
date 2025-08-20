import time
import itertools
import csv
import os

# Set limits
requests_per_day = 1500
requests_per_minute = 15
tokens_per_request = 500  # Estimated tokens per request
delay_between_requests = 4  # seconds

# Generate combinations (limit to 1500 per day)
age_ranges = ["0-10", "10-20", "20-30", "30-40", "40-50", "50-60", "60-70", "70+"]
genders = ["Male"]
clinical_histories = [
    "Smoking", "Asthma", "Diabetes", "Immunodeficiency",
    "Cardiovascular history", "acute bronchitis",
    "cocaine, heroin, or methamphetamines", "Family history of lung cancer",
    "genetic abnormalities in lungs", "allergies",
    "exposure to asbestos, coal dust, silica dust, or chemical fumes/toxins"
]
diseases = ["Pneumonia", "COPD", "Lung Cancer", "Asthma", "Tuberculosis or TB", "Covid-19"]

# Age-specific restrictions for diseases
disease_age_restrictions = {
    "0-10": ["COPD", "Lung Cancer", "Tuberculosis or TB"],
    "10-20": ["COPD", "Lung Cancer"],
    "60-70": ["Asthma", "Covid-19"],
    "70+": ["Pneumonia", "COPD"]
}

# Age-specific restrictions for clinical histories
clinical_history_age_restrictions = {
    "0-10": ["Smoking", "cocaine, heroin, or methamphetamines"],
    "10-20": ["Smoking", "cocaine, heroin, or methamphetamines"],
    "60-70": ["exposure to asbestos, coal dust, silica dust, or chemical fumes/toxins"],
    "70+": ["genetic abnormalities in lungs", "exposure to asbestos, coal dust, silica dust, or chemical fumes/toxins"]
}

# Clinical history restrictions
clinical_history_restrictions = [
    ("Smoking", "Asthma"),
    ("Smoking", "acute bronchitis"),
    ("Asthma", "acute bronchitis"),
    ("Genetic abnormalities in lungs", "Cardiovascular history"),
    ("Family history of lung cancer", "Genetic abnormalities in lungs")
]

# Generate combinations excluding "Normal" in pairs
clinical_history_combinations = [
    ", ".join(sorted(combo[:2]))  # Sort the histories for consistency
    for combo in itertools.combinations(clinical_histories, 2)
]
# Add "Normal" as a standalone option
clinical_history_combinations.append("Normal")

# Generate full combinations
combinations = itertools.product(age_ranges, genders, clinical_history_combinations, diseases)

# Function to enforce rate limiting
last_request_time = 0

def enforce_rate_limit():
    global last_request_time
    elapsed = time.time() - last_request_time
    if elapsed < (60 / requests_per_minute):  # Enforce 15 RPM
        time.sleep((60 / requests_per_minute) - elapsed)
    last_request_time = time.time()

# Function to estimate tokens in the prompt
def estimate_tokens(prompt):
    return len(prompt.split())  # Simplified token count estimation

# Write the CSV header
def write_csv_header():
    with open("medical_diagnosis_data.csv", mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Age", "Gender", "Clinical History", "Disease",
                         "Findings", "Blood Tests", "Prescriptions",
                         "Possible Causes", "Future Actions"])
    print("CSV Header Written")

# Write the data to CSV
def write_to_csv(data):
    with open("medical_diagnosis_data.csv", mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)
    print(f"{len(data)} rows written to CSV")

# Parse response into structured fields
def parse_response(response):
    sections = {
        "Findings": "N/A",
        "Blood Tests": "N/A",
        "Prescriptions": "N/A",
        "Possible Causes": "N/A",
        "Future Actions": "N/A",
    }

    current_section = None
    for line in response.split("\n"):
        line = line.strip()
        if line.startswith("### Findings"):
            current_section = "Findings"
        elif line.startswith("### Blood Tests"):
            current_section = "Blood Tests"
        elif line.startswith("### Prescriptions"):
            current_section = "Prescriptions"
        elif line.startswith("### Possible Causes"):
            current_section = "Possible Causes"
        elif line.startswith("### Future Actions"):
            current_section = "Future Actions"
        elif current_section and line:
            if sections[current_section] == "N/A":
                sections[current_section] = line
            else:
                sections[current_section] += f"\n{line}"

    return sections

# Load progress from the file
def load_progress():
    try:
        with open('progress_tracker.txt', 'r') as f:
            last_processed_index = int(f.read().strip())
            print(f"Resuming from index {last_processed_index}")
            return last_processed_index
    except FileNotFoundError:
        print("No progress file found. Starting from the beginning.")
        return 0

# Save progress to the file
def save_progress(index):
    with open('progress_tracker.txt', 'w') as f:
        f.write(str(index))
    print(f"Progress saved at index {index}")

# Query Gemini API with retries and timeout
def query_gemini_with_retry(age, gender, history, disease, retries=3):
    for attempt in range(retries):
        try:
            enforce_rate_limit()  # Ensure rate limiting
            prompt = f"""
            For a {gender} aged {age} with a clinical history of {history}, diagnosed with {disease}, provide:

            ### Findings
            List general findings related to the disease.

            ### Blood Tests
            Recommended blood tests.(recommend some for confirmation)

            ### Prescriptions
            Prescriptions with technical/medical terms.(give at least 5 drugs/medicines to recover/temporarily feel better)

            ### Possible Causes
            Mention possible causes of the disease.(include clinical history factors first and then others)

            ### Future Actions
            Provide the future course of action (procedures to follow).

            Ensure that you provide only medical information, no disclaimers or anything, just the information.
            Strictly generate results in the given headings format for all queries.
            """
            print(f"Calling API for: Age={age}, Gender={gender}, History={history}, Disease={disease}")
            response = genai.GenerativeModel("gemini-1.5-flash").generate_content(prompt)
            print("API response received")
            return response.text
        except Exception as e:
            print(f"Error on attempt {attempt + 1}: {e}")
            time.sleep(2)  # Wait before retrying

    return "Error: API call failed"

# Save results to CSV in batches
def save_to_csv(combinations, batch_size=50):
    buffer = []
    day_counter = load_progress()  # Start from where the previous session left off
    write_csv_header()  # Ensure headers are written once

    try:
        for idx, combo in enumerate(itertools.islice(combinations, day_counter, None)):
            if day_counter >= requests_per_day:
                print("Daily limit reached. Stopping.")
                break  # Stop after 1500 requests

            age, gender, clinical_history, disease = combo

            # Normalize clinical history order
            histories = tuple(sorted(clinical_history.split(", ")))

            # Skip invalid combinations due to age-disease restrictions
            if age in disease_age_restrictions and disease in disease_age_restrictions[age]:
                print(f"Skipping combination (disease-age restriction): Age={age}, Disease={disease}")
                continue

            # Skip invalid combinations due to age-clinical history restrictions
            if age in clinical_history_age_restrictions and any(h in clinical_history_age_restrictions[age] for h in histories):
                print(f"Skipping combination (clinical history-age restriction): Age={age}, Histories={histories}")
                continue

            # Skip invalid combinations due to clinical history restrictions
            if any(h1 in histories and h2 in histories for h1, h2 in clinical_history_restrictions):
                print(f"Skipping combination (clinical history restriction): Histories={histories}")
                continue

            # Debugging: Show valid combination being processed
            print(f"Processing combination {idx + 1}/{requests_per_day}: Age={age}, Gender={gender}, History={histories}, Disease={disease}")

            # Query the API and parse the response
            result = query_gemini_with_retry(age, gender, ", ".join(histories), disease)
            parsed_result = parse_response(result)

            # Append parsed data to buffer
            buffer.append([age, gender, ", ".join(histories), disease,
                           parsed_result["Findings"], parsed_result["Blood Tests"],
                           parsed_result["Prescriptions"], parsed_result["Possible Causes"],
                           parsed_result["Future Actions"]])

            # Write buffer to CSV in batches
            if len(buffer) >= batch_size:
                write_to_csv(buffer)
                buffer = []  # Clear buffer

            # Save progress every 50 combinations
            if (idx + 1) % 50 == 0:
                save_progress(idx + 1)
                print(f"Progress saved at index {idx + 1}")

            day_counter += 1

    finally:
        # Ensure remaining buffer is written
        if buffer:
            write_to_csv(buffer)
            print("Remaining data written to CSV")

        # Save progress after completing
        save_progress(day_counter)

# Execute the main function
save_to_csv(combinations)
# Importing libraries for EDA
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
# To ignore all the warnings
import warnings
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
# TfidfVectorizer converts a collection of raw documents (text) into a matrix of TF-IDF features. TF-IDF stands for Term Frequency-Inverse Document Frequency, which reflects the importance of a word in a document relative to a collection of documents.
from sklearn.metrics.pairwise import linear_kernel
#  linear_kernel is often used to calculate the similarity between samples in high-dimensional spaces efficiently.
from sklearn.metrics import accuracy_score
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from contextlib import redirect_stdout
import io

#Data filtering and Prepocessing
warnings.filterwarnings('ignore')

data = pd.DataFrame(pd.read_excel('MMT2_01.xlsx'))
null = data.isnull().sum()
data = data.drop(columns=['Uniq Id','Page Url','Crawl Timestamp','Flight Stops','Price Per Two Persons','Initial Payment For Booking','Cancellation Rules','Date Change Rules','Unnamed: 22', 'Unnamed: 23'])
data.isnull().sum()

"""## A total of 3633 values in the column Package Type are garbage Values and need to be deleted."""

# Deleting null values from the data
# 1. garbage values in the column Package Type
mask = data['Package Type'].str.contains('https://', na = False)
# mask variable makes a dataset of all values which contain https://
filtered = data[~mask]
# ~ is complement operator which only keeps the data entries which does not have any values with https://
df = filtered.dropna(subset = ['Hotel Details', 'Sightseeing Places Covered'])

# Copying the dataset for other data preprocessing processes
df2 = df.copy()
df2.isnull().sum()

df2['Airline'].value_counts()

# Use .loc to explicitly select the subset of data and fill missing values
df2['Airline'].replace('NaN', 'Personal Mode of Transportation', inplace=True)
df2.isnull().sum()




"""### Here as per the information generated and by seeing the datatype Collabrative Filtering which is best alogrithm for recommendation of continuous values we have to create some labels for some specific columns like:
### 1. Package Type
### 2. Start City
### 3. Mode of Transportation etc

### And there are some categorical values which will be part of recommendation which will be part of Content based filtering
### 1. Destination
### 2. Sightseeing Places Covered
### 3. Hotel Details etc
"""
df2['Package Label'] = df2['Package Type'].map({'Budget' : 0, 'Deluxe' : 1, 'Luxury' : 2, 'Premium' : 3, 'Standard' : 4})
df2['Start City Label'] = df2['Start City'].map({'Mumbai' : 0, 'New Delhi' : 1})

df2['PrimaryDestination'] = df2['Destination'].apply(lambda x:x.split('|')[0])

# Combine 'Package Type' and 'PrimaryDestination' into a single string
df2['Features'] =  df2['Package Type'] + " " + df2['PrimaryDestination']

# TF-IDF Vectorization
tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(df2['Features'])

# Compute the cosine similarity matrix
cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)



def get_recommendations(start_city, destination, package_type, person, want_airline, cosine_sim=cosine_sim):
    try:
        person = float(person)
    except ValueError:
        print(f"Error: 'person' must be a number, not '{person}'")
        return
    # Create a bold and larger font
    bold_font = ('Helvetica', 16, 'bold')

    # Construct a query feature string
    query_feature = package_type + " " + destination
    query_feature_vec = tfidf.transform([query_feature])

    # Compute similarity
    sim_scores = linear_kernel(query_feature_vec, tfidf_matrix).flatten()

    output_window = tk.Tk()
    output_window.title("Travel Recommendations")
    output_window.config(background="#87CEEB")  
    canvas = tk.Canvas(output_window, bg='#87CEEB', highlightbackground="#87CEEB" )
    scrollbar = ttk.Scrollbar(output_window, orient="vertical", command=canvas.yview)
    bigframe = ttk.Frame(canvas)

        # Configure the canvas to use the scrollbar
    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.create_window((0, 0), window=bigframe, anchor='nw')

    # Function to update the scrollregion
    def on_frame_configure(event):
        canvas.configure(scrollregion=canvas.bbox("all"))

    bigframe.bind("<Configure>", on_frame_configure)  
    if want_airline==True:
         # Get the indices of matching destinations
        matching_indices = [i for i, dest in enumerate(df2['Destination']) if destination in dest]
        # Select the packages with matching destinations and specified package type
        recommended_packages = df2.iloc[matching_indices]
        recommended_packages = recommended_packages[recommended_packages['Package Type'] == package_type]

        # Filter based on 'Start City' and 'Airline' preference
        recommended_packages = recommended_packages[recommended_packages['Start City'] == start_city]
        recommended_packages = recommended_packages[recommended_packages['Airline'] != 'Personal Mode of Transportation']
        
        for index, row in recommended_packages.iterrows():
            frame = ttk.Frame(bigframe, padding="10", relief=tk.RIDGE)
            frame.pack(fill='x', expand=True, pady=5)

            ttk.Label(frame, text=f"{row['Package Name']}",font=bold_font).pack(anchor='w')
            ttk.Label(frame, text=f"Destination: {row['Destination']}").pack(anchor='w')
            ttk.Label(frame, text=f"Itinerary: {row['Itinerary']}").pack(anchor='w')

            sightseeing_places = row['Sightseeing Places Covered'].split('|')
            for place in sightseeing_places:
                ttk.Label(frame, text=f"- {place.strip()}").pack(anchor='w')
            ttk.Label(frame, text=f"Airlines: {row['Airline']}").pack(anchor='w')
            tot_price=row['Per Person Price']*person
            ttk.Label(frame, text=f"Total amount: {tot_price}").pack(anchor='w')
            ttk.Label(frame, text=f"Per Person Price: {row['Per Person Price']}",font=bold_font).pack(anchor='e')
        
    else:
         # Get the indices of matching destinations
        matching_indices = [i for i, dest in enumerate(df2['Destination']) if destination in dest]
        # Select the packages with matching destinations and specified package type
        recommended_packages = df2.iloc[matching_indices]
        recommended_packages = recommended_packages[recommended_packages['Package Type'] == package_type]

        # Filter based on 'Start City' and 'Airline' preference
        recommended_packages = recommended_packages[recommended_packages['Start City'] == start_city]
        
        for index, row in recommended_packages.iterrows():
            frame = ttk.Frame(bigframe, padding="10", relief=tk.RIDGE)
            frame.pack(fill='x', expand=True, pady=5)

            ttk.Label(frame, text=f"{row['Package Name']}",font=bold_font).pack(anchor='w')
            ttk.Label(frame, text=f"Destination: {row['Destination']}").pack(anchor='w')
            ttk.Label(frame, text=f"Itinerary: {row['Itinerary']}").pack(anchor='w')

            sightseeing_places = row['Sightseeing Places Covered'].split('|')
            for place in sightseeing_places:
                ttk.Label(frame, text=f"- {place.strip()}").pack(anchor='w')
            amt=row['Per Person Price']*person
            ttk.Label(frame, text=f"Total amount: {amt}").pack(anchor='w')
            ttk.Label(frame, text=f"Per Person Price: {row['Per Person Price']}",font=bold_font).pack(anchor='e')
        
 
    scrollbar.pack(side="right", fill="y")
    canvas.pack(padx=350,side="left", fill="both", expand=True)
    output_window.mainloop()
        
    
def resize_image(event):
    new_width = root.winfo_width()
    new_height = root.winfo_height()
    image = original_image.resize((new_width, new_height))
    photo = ImageTk.PhotoImage(image)
    background_label.config(image=photo)
    background_label.image = photo  # avoid garbage collection

# Create the main window
root = tk.Tk()
root.title("Intelligent Travel Planning with Budget Optimization")

# Load the background image
original_image = Image.open('background3.png')
photo = ImageTk.PhotoImage(original_image)

# Create a background label to hold the image
background_label = tk.Label(root, image=photo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Bind the resize event to the resize_image function
root.bind('<Configure>', resize_image)

# Create a label for the title and place it above the frame
title_label = tk.Label(root, text="Intelligent™ Travel Planning with\nBudget Optimization", font=("Helvetica", 24, 'bold'))
title_label.pack(padx=1,pady=10)

# Create a frame for the input fields (use a transparent background)
frame = tk.Frame(root, bg='white')
frame.pack(padx=20, pady=20, expand=True)

# From City dropdown
from_city_label = tk.Label(frame, text="From City", bg="white", fg="black")
from_city_label.grid(row=0, column=0, padx=10, pady=5)
from_city_option = ttk.Combobox(frame, values=["Mumbai","New Delhi"])
from_city_option.grid(row=1, column=0, padx=10, pady=5)
from_city_option.set("Select Option")


# Destination 
to_city_label = tk.Label(frame, text="Destination", bg="white", fg="black")
to_city_label.grid(row=0, column=1, padx=10, pady=5)
to_city_entry = tk.Entry(frame)
to_city_entry.grid(row=1, column=1, padx=10, pady=5)


#Package Type entry
package_label = tk.Label(frame, text="Package Type", bg="white", fg="black")
package_label.grid(row=0, column=2, padx=10, pady=5)
package_entry = tk.Entry(frame, bg="white", fg="black")
package_entry.grid(row=1, column=2, padx=10, pady=5)


# Departure Date entry
departure_date_label = tk.Label(frame, text="Departure Date", bg="white", fg="black")
departure_date_label.grid(row=0, column=3, padx=10, pady=5)
departure_date_entry = tk.Entry(frame,bg="white", fg="black")
departure_date_entry.insert(tk.END, "      DD/MM/YYYY")
departure_date_entry.grid(row=1, column=3, padx=10, pady=5)

# Guests entry
guests_label = tk.Label(frame, text="Guests", bg="white", fg="black")
guests_label.grid(row=0, column=4, padx=10, pady=5)
guests_entry = tk.Entry(frame, bg="white", fg="black")
guests_entry.grid(row=1, column=4, padx=10, pady=5)


# Radio button for flight search
flight_search_var = tk.BooleanVar()
flight_search_radio = tk.Radiobutton(frame, text="I'm looking for flights", variable=flight_search_var, value=True)
flight_search_radio.grid(row=2, columnspan=1, padx=10, pady=5)

#calling the output
def call():
    start_city=from_city_option.get()
    destination=to_city_entry.get()
    package_type=package_entry.get()
    tot_person=guests_entry.get()
    flight=flight_search_var.get()
    # Call the user-defined function that generates the travel recommendation output
    output = get_recommendations(start_city,destination,package_type,tot_person,flight, True)

title_label = tk.Label(root, text="All copyrights reserved", font=("Helvetica", 10, 'bold', 'italic'))
title_label.pack(padx=3, anchor='e')
    
# Submit button
submit_button = tk.Button(frame, text="Submit", bg='purple', fg='white', command=call)
submit_button.grid(row=3, columnspan=12, padx=8, pady=6)

# Run the application
root.mainloop()
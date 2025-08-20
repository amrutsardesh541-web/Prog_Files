import numpy as np
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

# Existing data
temperature = np.array([20, 25, 30, 35, 40, 45, 50, 55, 60, 65])
weather_labels = np.array(['0', '0', '1', '2', '2', '2', '1', '0', '0', '1'])

# Generate additional random temperatures within the range of 15 to 40 degrees Celsius
additional_temperatures = np.random.randint(15, 41, size=90)
# Generate corresponding weather labels based on the temperature range
additional_weather_labels = []
for temp in additional_temperatures:
    if temp < 25:
        additional_weather_labels.append('0')  # Rainy
    elif temp < 35:
        additional_weather_labels.append('1')  # Cloudy
    else:
        additional_weather_labels.append('2')  # Sunny

# Concatenate the additional data with the existing data
temperature = np.concatenate([temperature, additional_temperatures])
weather_labels = np.concatenate([weather_labels, additional_weather_labels])

# Reshape the data for Decision Tree classifier
X = temperature.reshape(-1, 1)
y = weather_labels

# Train a Decision Tree Classifier
model = DecisionTreeClassifier()
model.fit(X, y)

# Make predictions for a range of temperatures
predicted_temperatures = np.arange(15, 41, 1).reshape(-1, 1)
predicted_weather = model.predict(predicted_temperatures)

# Plot the results (line chart with predicted and actual scores)
plt.figure(figsize=(10, 6))
plt.plot(predicted_temperatures, predicted_weather, marker='o', linestyle='-', color='b', label='Predicted Weather')
plt.plot(temperature, y, marker='x', linestyle='', color='r', label='Actual Weather')
plt.title('Predicted vs Actual Weather Based on Temperature')
plt.xlabel('Temperature')
plt.ylabel('Weather')
plt.yticks(np.unique(predicted_weather), ['Rainy', 'Cloudy', 'Sunny'])  # Set y-axis ticks to display weather categories
plt.legend()
plt.grid(True)
plt.show()

# Initialize lists to store accuracy values
accuracies = []

# Define the number of iterations (test sets) you want to run
num_iterations = 10

# Train and evaluate the model over multiple test sets
for _ in range(num_iterations):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
    model = DecisionTreeClassifier()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    accuracies.append(accuracy)

# Plot the accuracy over multiple test sets (line chart)
plt.figure(figsize=(10, 6))
plt.plot(range(1, num_iterations + 1), accuracies, marker='o', color='b', linestyle='-')
plt.title('Accuracy Over {} Test Sets'.format(num_iterations))
plt.xlabel('Test Set Number')
plt.ylabel('Accuracy')
plt.xticks(range(1, num_iterations + 1))
plt.grid(True)
plt.show()

# Calculate correct and incorrect predictions
correct_predictions = (y_pred == y_test).sum()
incorrect_predictions = len(y_test) - correct_predictions

# Plot a pie chart to show the distribution of correct and incorrect predictions
labels = ['Correct Predictions', 'Incorrect Predictions']
sizes = [correct_predictions, incorrect_predictions]
colors = ['#ff9999','#66b3ff']
explode = (0.1, 0)  # explode 1st slice

plt.figure(figsize=(7, 7))
plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
plt.title('Prediction Accuracy')
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()

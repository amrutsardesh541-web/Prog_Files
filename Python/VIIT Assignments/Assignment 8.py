# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 09:18:49 2024

@author: Piyus
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split



# Define temperature range
temperature = np.random.randint(15, 41, size=100)  # Generating 100 random temperatures between 15 and 40

# Initialize an empty list to store weather values
weather = []

# Define ranges for each weather category
weather_ranges = {
    'Sunny': (30, 45),  # Define range for Sunny weather
    'Rainy': (15, 25),  # Define range for Rainy weather
    'Windy': (25, 30)   # Define range for Windy weather
}

# Assign weather values based on temperature ranges
for temp in temperature:
    chosen_weather = None
    for category, (min_temp, max_temp) in weather_ranges.items():
        # Introduce randomness in weather assignment
        if np.random.rand() < 0.8:  # Adjust this threshold to control accuracy
            if min_temp <= temp <= max_temp:
                chosen_weather = category
                break
    if chosen_weather is None:
        # If no weather category is assigned, choose randomly
        chosen_weather = np.random.choice(list(weather_ranges.keys()))
    weather.append(chosen_weather)

# Create DataFrame
df = pd.DataFrame({'Temperature': temperature, 'Weather': weather})

# Display sample of the dataset
print(df.head())

X = df[['Temperature']]
y = df['Weather']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 20)

clf = DecisionTreeClassifier()
clf.fit(X_train, y_train)

y_pred = clf.predict(X_test)
print('Accuracy is ', accuracy_score(y_test, y_pred))

cor_pred = (y_pred==y_test).sum()
incor_pred = len(y_test) - 1
slices = [cor_pred, incor_pred]
labels = ['Correct Prediction', 'Incorrect Predictions']
plt.title('Accuracy: {:.2f}%'.format(accuracy_score(y_test, y_pred) * 100))
plt.pie(slices, labels = labels)
plt.show()

# Initialize lists to store accuracy values
accuracies = []

# Define the number of iterations (test sets) you want to run
num_iterations = 10

for _ in range(num_iterations):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
    clf = DecisionTreeClassifier()
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    accuracies.append(accuracy)

# Line chart
plt.figure(figsize=(10, 6))
plt.plot(range(1, num_iterations + 1), accuracies, marker='o', color='b', linestyle='-')
plt.title('Accuracy Over {} Test Sets'.format(num_iterations))
plt.xlabel('Test Set Number')
plt.ylabel('Accuracy')
plt.xticks(range(1, num_iterations + 1))
plt.grid(True)
plt.show()

# Generate a range of temperature values for prediction
temperature_values = np.linspace(15, 40, num=100).reshape(-1, 1)

# Predict weather for the temperature values
predicted_weather = clf.predict(temperature_values)

# Line chart for predicted weather based on temperature
plt.figure(figsize=(10, 6))
plt.plot(temperature_values, predicted_weather, marker='o', linestyle='-', color='b')
plt.title('Predicted Weather Based on Temperature')
plt.xlabel('Temperature')
plt.ylabel('Predicted Weather')
plt.yticks(np.arange(len(weather_ranges)), list(weather_ranges.keys()))  # Set y-axis ticks to display weather categories
plt.grid(True)
plt.show()



# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 09:10:29 2024

@author: Piyus
"""

import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file into a DataFrame
df = pd.read_csv('exams.csv')
print(df)

# Assuming your CSV has a column named 'math_score', replace it with the actual column name in your file
math_scores = df['math score']

# Calculate the mode
mode_value = math_scores.mode().values[0]

# Get unique values and their counts using value_counts()
value_counts = math_scores.value_counts()

# Create a bar plot for unique values
plt.bar(value_counts.index, value_counts.values, color='blue',  label='Unique Values')

# Highlight the mode value with a different color
plt.bar(mode_value, value_counts[mode_value], color='red', label='Mode')

# Set labels and title
plt.xlabel('Math Score')
plt.ylabel('Frequency')
plt.title('Math Scores Distribution with Mode Highlighted')

# Add legend
plt.legend()

# Show the plot
plt.show()


# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 14:34:52 2024

@author: Piyus
"""

# Survey five friends about their favorite colors. Present the results in a simple table or list
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load DataFrame from Excel file
df = pd.read_excel('Assign6_2.xlsx')

# Drop 'Timestamp' and 'Name' columns
df.drop(columns=['Timestamp', 'Name'], inplace=True)

# Count the occurrences of each color
color_counts = df['Your Favorite Color'].value_counts()

# Get unique color values
unique_colors = df['Your Favorite Color'].unique()

# Combine colors with less than 3% occurrence into 'Others'
threshold = 0.03
others_count = color_counts[color_counts / len(df) < threshold].sum()
color_counts = color_counts[color_counts / len(df) >= threshold]
color_counts['Others'] = others_count

# Count the occurrences of each color
ele_unique = df['Preferred color for Electronics and Smartphones'].unique()
ele_counts = df['Preferred color for Electronics and Smartphones'].value_counts()

# Plotting pie chart
sns.set_style("whitegrid")  # Setting seaborn style
plt.pie(color_counts, labels=color_counts.index, autopct='%1.1f%%')
plt.title('Favorite Color of Friends')
plt.show()

# Plotting bar graph
sns.barplot(x=ele_unique, y=ele_counts)
plt.xlabel('Color')
plt.ylabel('Frequency')
plt.title('Most Loved Color for electronics and smartphones')
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability if needed
plt.show()

#Plotting Countplot
sns.countplot(x='Preferred color for vehicles', data=df, hue='Gender')
plt.show()


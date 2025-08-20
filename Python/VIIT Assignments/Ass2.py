# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 08:55:11 2024

@author: Piyus
"""
# Importing all Libraries
import pandas as pd
import matplotlib.pyplot as plt
import random

#Taking Minimum and Maximum numbet of steps
lb = int(input("Enter min steps: "))
ub = int(input("Enter max steps: "))

# Create a datframe by using DataFrame() in-built function
df = pd.DataFrame({
    "Days": range(1, 31),
    "No. of steps": [random.randint(lb, ub) for i in range(30)]
})

# Printing dataset
print(df)

# Plotting plots 
plt.plot(df["Days"], df["No. of steps"], marker = '.', color = 'red')
plt.xlabel("Days")
plt.ylabel("No. of steps")
plt.title("Daily Steps")

for i, row in df.iterrows():
    plt.annotate(f'({row["No. of steps"]})', 
                 (row['Days'],row['No. of steps']),
                 textcoords="offset points",
                 xytext=(0,10),
                 fontsize=9,
                 color = 'black')
plt.show()




+
"""
Conclusion :- The output shows a line graph which shows No. of steps per day with proper label to x-axis and y-axis and heading to Graph. 
"""

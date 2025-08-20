# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 08:25:38 2024

@author: Piyus
"""
# importing necessary python libraires
import pandas as pd
import matplotlib.pyplot as plt

# Reading all data from csv file
data = pd.read_csv('exams.csv')
df = pd.DataFrame(data)

# Dropping unecssary columns
print(df.drop(['race/ethnicity', 'parental level of education', 'lunch', 'test preparation course'], axis = 1))
math_score = df['math score']

# FindingAverage of the math scores
print("Average of math score is", math_score.mean())

# Calculationg mode of the math scores.
mode = math_score.mode().values[0]
print("Mode is ", mode)

# Plotting graphs
plt.figure(figsize = (15, 8))
unique_values = math_score.value_counts()
plt.bar(unique_values.index, unique_values.values, label = 'Marks')
plt.bar(mode, unique_values[mode], label = 'Mode')
plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.legend()


"""
From the above data set we get the following insights:-
1) Average math scores is 68.67.
2) Mode is 78
3) Majority of the students have scored marks in the range of 62 - 85.
4) This shows that paper difficulty level was moderate
"""

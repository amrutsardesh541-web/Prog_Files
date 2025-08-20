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

#EDA
counts = df2['Package Type'].value_counts()
fig = go.Figure([go.Bar(x=counts.index, y=counts.values)])
fig.update_layout(title='Package Type Counts')
fig.show()

#This graph gives price distribution for each Package type
fig = px.box(df2, x='Package Type', y='Per Person Price', title='Per Person Price Distribution by Package Type')
fig.show()

# Convert non-numeric columns to categorical data type
for col in df.columns:
    if df[col].dtype == 'object':
        df[col] = df[col].astype('category')

# Convert categorical columns to numerical using label encoding
for col in df.select_dtypes(include=['category']).columns:
    df[col] = df[col].cat.codes

# Calculate the correlation matrix
corr_matrix = df.corr()

# Create a heatmap using seaborn
plt.figure(figsize=(10, 8))
sns.heatmap(corr_matrix, annot=True, cmap='inferno')
plt.title('Correlation Heatmap')
plt.show()

# Combine 'Package Type' and 'PrimaryDestination' into a single string
df2['Features'] =  df2['Package Type'] + " " + df2['PrimaryDestination']

# TF-IDF Vectorization
tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(df2['Features'])

# Compute the cosine similarity matrix
cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)



def get_recommendations(start_city, destination, package_type, want_airline, cosine_sim=cosine_sim):
    # Construct a query feature string
    query_feature = package_type + " " + destination
    query_feature_vec = tfidf.transform([query_feature])

    # Compute similarity
    sim_scores = linear_kernel(query_feature_vec, tfidf_matrix).flatten()

    # Get the indices of matching destinations
    matching_indices = [i for i, dest in enumerate(df2['Destination']) if destination in dest]

    # Select the packages with matching destinations and specified package type
    recommended_packages = df2.iloc[matching_indices]
    recommended_packages = recommended_packages[recommended_packages['Package Type'] == package_type]

    # Filter based on 'Start City' and 'Airline' preference
    recommended_packages = recommended_packages[recommended_packages['Start City'] == start_city]
    if not want_airline:
        recommended_packages['Airline'] = 'Not Included'

    for index, row in recommended_packages.iterrows():
        print("Package Name:", row['Package Name'])
        print("Destination:", row['Destination'])
        print("Primary Destination:", row['PrimaryDestination'])  # Access primary destination
        print("Itinerary:", row['Itinerary'])
        sightseeing_places = row['Sightseeing Places Covered'].split('|')
        for place in sightseeing_places:
            print("-", place.strip())  # Remove leading/trailing whitespaces
        print("Per Person Price:", row['Per Person Price'])
        print("\n")  # Add a newline between packages

# Example usage
start_city_input = input("Enter starting city: ")
destination_input = input("Enter destination: ")
package_type_input = input("Enter package type: ")


get_recommendations(start_city_input, destination_input, package_type_input, True)
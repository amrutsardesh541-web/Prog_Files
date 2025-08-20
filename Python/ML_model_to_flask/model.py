# -*- coding: utf-8 -*-
"""
Created on Sun Aug 11 19:49:04 2024

@author: Piyus
"""

import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import pickle

# load csv file
df = pd.read_csv('Iris.csv')
#print(df.info())
#print(df)

# Select dependant and independant variables 
X = df[['SepalLengthCm','SepalWidthCm','PetalLengthCm','PetalWidthCm']]
y = df['Species']

# training and spliting the dataset
X_train,X_test,y_train,y_test = train_test_split(X, y, test_size=0.2, random_state=50)

# Feature Scaling
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

# Modelling 
classifier = RandomForestClassifier()
classifier.fit(X_train, y_train)

# Make pickle file of the model
pickle.dump(classifier, open("model.pkl","wb"))
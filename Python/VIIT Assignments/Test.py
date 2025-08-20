# -*- coding: utf-8 -*-
"""
Created on Sat Jan 27 16:24:43 2024

@author: Piyus
"""

import pandas as pd
import numpy as np
import seaborn as sns
df = pd.read_csv('data.csv')
print(df)
sns.boxplot(x="Country", y="UnitPrice", data=df)
country_num = df["Country"].value_counts()
print(country_num)
country = df["Country"].unique()
print(country)
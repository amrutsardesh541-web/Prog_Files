# -*- coding: utf-8 -*-
"""
Created on Sun Feb 11 16:28:33 2024

@author: Piyus
"""

import pandas as pd
df = pd.DataFrame(pd.read_excel("Amazon.xlsx"))
df.isnull().sum()
print(df)
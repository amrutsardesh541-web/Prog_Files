# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 19:49:30 2024

@author: Piyus
"""

import numpy as np

arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print(arr)
m = int(input("Enter row "))
n = int(input("Enter element number "))
print("Your element is", arr[m, n])
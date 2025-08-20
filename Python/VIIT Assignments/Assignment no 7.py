# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 08:24:53 2024

@author: Piyus
"""

import string
import matplotlib.pyplot as plt
para = 'My name is Piyush deshmukh and I love my family and my country ny favourite number is 12345678765432100000999999.'

lower = para.lower()
print(lower)
letter_counts = {letter : lower.count(letter) for letter in string.ascii_lowercase}
number_counts = {number : number.count(number) for number in string.digits}
plt.bar(letter_counts.keys(), letter_counts.values(), color = 'red')
plt.bar(number_counts.keys(), number_counts.values(), color = 'blue')
plt.xlabel('Letter and Numbers')
plt.ylabel('Frequency')
plt.title('Count the number of times each letter appears in a paragraph of text. Display the frequencies in a bar chart')
plt.show()
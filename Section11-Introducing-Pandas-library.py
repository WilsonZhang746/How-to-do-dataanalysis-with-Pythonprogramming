# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 12:45:46 2022
How to do data analysis with Python programming

@author: https://www.youtube.com/@easydatascience2508
"""


### Section 11. Introducing The Pandas library
##Lecture 1. Getting started with pandas

import pandas as pd
import numpy as np



# ### Declaring a Series 

s = pd.Series([12, -4, 7, 9])
s


s = pd.Series([12, -4, 7, 9], index=['a', 'b', 'c', 'd'])
s


s.values


s.index


# Defining a DataFrame

data = {'color' : ['blue', 'green', 'yellow', 'red', 'white'],
        'object' : ['ball', 'pen', 'pencil', 'paper', 'mug'],
        'price' : [1.2, 1.0, 0.6, 0.9, 1.7]}
frame = pd.DataFrame(data)
frame











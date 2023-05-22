# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26,2023 

@author: Khai Le
Title: Curve fit using Ridge OR Linear Regression method from Lecture 4
"""

import numpy as np
import matplotlib.pyplot as plt

from sklearn.linear_model import Ridge,LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline

# Check if import the correct csv file
'''
with open("pp.csv","r") as f:
    print(f.readline())
    print(f.readline())
    f.close()'''

x=[]
y=[]
with open("pp.csv", "r") as f:
    f.readline() # throw away first line
    for l in f:
        l.strip()
        things=l.split(",") #seperate different data
        x.append([float(things[0])]) #call first column in file
        y.append([float(things[1])]) #call second column in file
    f.close()
    
# Check that we get correct data
print(x[:5])
print(y[:5])

model = make_pipeline(PolynomialFeatures(5), Ridge())
model.fit(x, y)
y_plot = model.predict(x)

plt.plot(x,y)
plt.plot(x,y_plot)
plt.show()

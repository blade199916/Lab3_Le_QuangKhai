# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26, 2023

@author: Quoc Cao
Title: Curve fit using Polynomial Regression method from Lecture 1
"""

import numpy as np
import scipy.optimize as opt
import scipy.stats as st
import math
import matplotlib.pyplot as plt

x = np.arange(-3,3.1, 0.1) #generates a range of values from -3 to 3.1 (excluding 3.1) in steps of 0.1
y = [-34, -29.507, -25.416, -21.709, -18.368, -15.375, -12.712, -10.361, -8.304, -6.523, -5, -3.717, -2.656, -1.799, -1.128, -0.625, -0.272, -0.051, 0.056, 0.067, 0, -0.127, -0.296, -0.489, -0.688, -0.875, -1.032, -1.141, -1.184, -1.143, -1, -0.737, -0.336, 0.221, 0.952, 1.875, 3.008, 4.369, 5.976, 7.847, 10, 12.453, 15.224, 18.331, 21.792, 25.625, 29.848, 34.479, 39.536, 45.037, 51, 57.443, 64.384, 71.841, 79.832, 88.375, 97.488, 107.189, 117.496, 128.427, 140]

#   equation: y=3*x^3 + 6*x^2 +2*x - 1)
    


def pres(order):
    
    p = np.poly1d(np.polyfit(x, y, order))
    ypred = [p(v) for v in x]
    plt.plot(x, y, 'r', label = "orig")
    plt.plot(x, ypred, 'g', label = "pred")
    #add a title, legend, and grid lines to the plot
    plt.title("Fit for order {}".format(order))
    plt.legend()
    plt.grid()
    plt.show()
    return p
pres(3) #which fits a third-order polynomial 


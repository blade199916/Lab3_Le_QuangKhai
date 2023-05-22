# -*- coding: utf-8 -*-
"""
Created on Feb 26, 2023

@author: Quang Khai Le
Title: Curve fit using Polynomial Regression method from Lecture 1
"""

import numpy as np
import scipy.optimize as opt
import scipy.stats as st
import math
import matplotlib.pyplot as plt

x = np.arange(-5.2,8.5, 0.2) #generates a range of values from -5.2 to 0.2 form 0.2 increment
y = [3102.776, 2634, 2220.44,1857.584,1541.112,1266.896,1031,829.68,659.384,516.752,398.616,302,224.12,162.384,114.392,77.936,51,31.76,18.584,10.032,4.856,2
,0.6,-0.016,-0.328,-0.624,-1,-1.36,-1.416,-0.688,1.496,6,13.88,26.384,44.952,71.216,107,154.32,215.384,292.592,388.536,506,647.96,817.584,1018.232
,1253.456,1527,1842.8,2204.984,2617.872,3085.976,3614,4206.84,4869.584,5607.512,6426.096,7331,8328.08,9423.384,10623.152,11933.816,13362,14914.52,16598.384,18420.792,20389.136,22511,24794.16,27246.584]

#for i in range(len(x)):
#    y.append(5*x[i]**4 + 4*x[i]**3 -2*x[i] - 1)
    


def pres(order):
    
    p = np.poly1d(np.polyfit(x, y, order))
    ypred = [p(v) for v in x]
    plt.plot(x, y, 'r', label = "orig")
    plt.plot(x, ypred, 'g', label = "pred")
    #add a title, legend, and grid lines to the plot
    plt.title("fit for order {}".format(order))
    plt.legend()
    plt.grid()
    plt.show()
    return p
pres(4) #which fits a fourth-order polynomial 


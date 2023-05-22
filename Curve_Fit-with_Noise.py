# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26,2023 

@author: Quang Khai Le
Title: Curve Fit with Noise from Lecture 2
"""
import numpy as np
import scipy.optimize as opt
import math
import matplotlib.pyplot as plt
import scipy.stats as st
import random

def fds(xin, a, b, c, d):#generate sin wave
    return[(a/(b+xin))*math.sin(3*xin*math.pi/c)+d for xin in x]

x = [xin/10 for xin in range(400)]
y = fds(x, 3, 3, 3, 3)

popt,pcov = opt.curve_fit (fds, x, y)#curve fit of the data
# Plot the original sine wave
yy = [y+random.gauss(0,0.1)for y in y]#value of noise
plt.plot(x, y, 'b')
plt.scatter(x, yy, alpha =0.3, s=3, c='red')
plt.show()

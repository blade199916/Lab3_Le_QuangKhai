# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26,2023 

@author: Khai Le
Title: Damped Sine Wave Curve Fit from Lecture 2
"""

import numpy as np
import scipy.optimize as opt
import math
import matplotlib.pyplot as plt

def fds(xin, a, b, c, d):#generate sin wave
    return[(a/(b+xin))*math.sin(3*xin*math.pi/c)+d for xin in x]

x = [xin/10 for xin in range(400)]
y = fds(x, 3, 3, 3, 3)

popt,pcov = opt.curve_fit (fds, x, y)
# Plot the original sine wave
plt.plot(x,y,'-r',label="original")
plt.legend()
plt.show()

# Plot the fitted waveform
plt.plot(x,y,'-r',label="original")
plt.plot(x,fds(x,*popt),'-b',label="SineFit")
plt.title("Damped Sine Wave Curve Fit")
plt.legend()
plt.show()

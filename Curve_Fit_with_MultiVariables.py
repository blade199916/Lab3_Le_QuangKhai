# -*- coding: utf-8 -*-
"""

@author: Quang Khai Le
Title: Curve Fit with Multi-Variables from Lecture 3
"""

import math
import numpy as np
import scipy.optimize as opt
import scipy.integrate as integ
import matplotlib.pyplot as plt

x0=[x/10 for x in range (100)]
x1= [math.cos(x/10)for x in range (100)]
xa=(x0,x1)

def rf(X,fx0,fx1):
    x0,x1=X
    rv=np.sin(np.multiply(x0, fx0)+np.sin(np.multiply(x1, fx1)))#generate y values
    return rv
yv=rf((x0,x1),2,3)
plt.plot(yv)
plt.show()

def Test(h0,h1):
    popt,pcov=opt.curve_fit(rf,xa,yv,(h0,h1))
    plt.title("Curve Fit with Multi-Variables: {},{}" .format(h0, h1))
    plt.plot(rf((x0,x1),2,3),color="b", label=('original'))
    plt.plot(rf((x0,x1),*popt),color="g", label=('Fitted curve'))
    plt.legend()
    plt.show()

# Start testing
Test(32,32)#did not work
Test(13,13)#did not work
Test(2,1)#work well
Test(3,5)#a bit large
Test(6,4)# still large
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 01:21:44 2022

@author: user
"""

import numpy as np
import matplotlib.pyplot as plt

"""
def my_gauss(x, sigma=0.5, h=1.5, mid=6):    
    variance = pow(sigma, 2)
    return h * np.exp(-pow(x-mid, 2)/(2*variance))

x = np.arange(0,4*np.pi,0.1)   # start,stop,step
y = -(np.tanh(x-5))+1

plt.plot(x,my_gauss(x),color = 'blue', label= 'neutral particle source')
plt.plot(x,y, color= 'orange', label= 'electron density')
plt.title('Illustration of neutral transport',fontdict={"family":"Times New Roman","size": 18})
plt.legend()

"""

x = np.arange(500,3500,500)   # start,stop,step
y = x
#y = -pow(np.cosh(x-5),-2)

plt.plot(x,y,color = 'orange', label= 'gradiant of density')
plt.title('gradiant of density',fontdict={"family":"Times New Roman","size": 18})
plt.legend()
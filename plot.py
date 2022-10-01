# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import matplotlib.pyplot as plt

exp_file = np.genfromtxt('yag_27205_275.dat',delimiter=' ')

psi_n = exp_file[:,0]
plt.plot(exp_file[:,0], exp_file[:,2])
plt.show()

data_file = np.genfromtxt('ne3da.txt',delimiter=',')

R_Rsep = data_file[:,0]
plt.plot(data_file[:,0], data_file[:,1])
plt.show()



# -*- coding: utf-8 -*-
"""
Created on Tue Nov  8 23:02:46 2022

@author: user
"""

import numpy as np
import pickle

exp_file = np.genfromtxt('C:/Users/user/Documents/SOLPS data/simulation data/mast/yag_27205_275.dat',delimiter=' ')

psi_n = []
exp_ne = []
err_ne =[]

j=1

while j< 60:
    a = exp_file[j,0]
    psi_n.append(a)
    b = exp_file[j,2]
    exp_ne.append(b)
    c = exp_file[j,4]
    err_ne.append(c)
    j= j+ 1

new_exp = [psi_n, exp_ne, err_ne]

with open("my_pickle.pkl", "wb") as f:
    pickle.dump(new_exp, f)

with open("192012_3250_e8099.pkl","rb") as pkl_example:
    myexample = pickle.load(pkl_example)




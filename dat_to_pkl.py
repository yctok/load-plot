# -*- coding: utf-8 -*-
"""
Created on Tue Nov  8 23:02:46 2022

@author: user
"""

import numpy as np
import pickle

exp_file = np.genfromtxt('yag_27205_275.dat',delimiter=' ')

psi_n = []
exp_ne = []
err_ne =[]
exp_te = []
err_te = []

j=0

while j< 60:
    a = exp_file[j,0]
    psi_n.append(a)
    b = exp_file[j,2]
    exp_ne.append(b)
    c = exp_file[j,4]
    err_ne.append(c)
    d = exp_file[j,10]
    exp_te.append(d)
    e = exp_file[j,16]
    err_te.append(e)  
    j= j+ 1

psi_dat = {'psi_data': psi_n}
ne_dat = {'electron_density': exp_ne, 'electron_density_error': err_ne}
te_dat = {'electron_temperature': exp_te, 'electron_temperature_error': err_te}

mast_dat = {'psi_data': psi_dat, 'density_data': ne_dat, 'temperature_data': te_dat}

with open("my_pickle.pkl", "wb") as f:
    pickle.dump(mast_dat, f)

with open("192012_3250_e8099.pkl","rb") as pkl_example:
    myexample = pickle.load(pkl_example)




# -*- coding: utf-8 -*-
"""
Created on Sat Oct  1 00:34:46 2022

@author: user
"""

import numpy as np
import matplotlib.pyplot as plt
import re

file ='C:/Users/user/Documents/SOLPS data/simulation data/mast/g027205.00275.X2.equ'

with open(file) as f:
     datalist =f.readlines()

j= 17

while j< 43:
    string2 = datalist[j]
    gdata = re.findall('[-+]?\d+\.?\d+[eE]?[-+]\d+', string2)
    mylist =[]
    for ii in gdata:
        a = np.float64(ii) +np.float64(1.00000000)
        b = "{:.8E}".format(a)
        mylist.append(b)
    writelist = ' '.join(str(x)+"   " for x in mylist)
    datalist[j] = "\t" + writelist + "\n"
    j= j+ 1

file2 = 'C:/Users/user/Documents/SOLPS data/simulation data/mast/g027205.00275.X2_m.equ'
with open(file2,'w') as g:
    for i,line in enumerate(datalist,0):         ## STARTS THE NUMBERING FROM 1 (by default it begins with 0)    
        g.writelines(line)
        
"""

newstring ="tdata(1, 2, 1, 1)= -0.0975, tdata(2, 2, 1, 1)= 0.53796,"
ndata = re.findall('[-+]?[.]?[\d]+(?:,\d\d\d)*[\.]?\d*(?:[eE][-+]?\d+)?', newstring)
ndatap = re.findall('[-+]?\d+\.?\d+', newstring)
print(ndatap)

string2 ="0.59999999E-01    0.75156251E-01    0.90312503E-01    0.10546875E+00    0.12062500E+00"

gwrite = re.sub('[-+]?\d+\.?\d+[eE]?[-+]\d+', '3.12345678e-03', string2)
print(gwrite)

"""

w_file ='C:/Users/user/Documents/SOLPS data/simulation data/mast/vvfile.ogr'

with open(w_file) as wf:
     w_datalist = wf.readlines()

for m, k in enumerate(w_datalist):
#for m in range(10):
    string_w = w_datalist[m]
    w_data = re.findall('[-+]?\d+\.?\d+', string_w)  
    a = np.float64(w_data[0]) + np.float64(1000.00000)
    a1 = "{: .5f}".format(a)
    b = np.float64(w_data[1])
    b1 = "{: .5f}".format(b)
    w_list =[]
    w_list.append(a1)
    w_list.append(b1)
    w_writelist = ' '.join(str(y)+ "\t  " for y in w_list)
    w_datalist[m] = "  " + w_writelist + "\n"
   
 
w_file2 = 'C:/Users/user/Documents/SOLPS data/simulation data/mast/vvfile_m.ogr'
with open(w_file2,'w') as wg:
    for l,w_line in enumerate(w_datalist):         ## STARTS THE NUMBERING FROM 1 (by default it begins with 0)    
        wg.writelines(w_line)

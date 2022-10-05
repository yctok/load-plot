# -*- coding: utf-8 -*-
"""
Created on Sat Oct  1 00:34:46 2022

@author: user
"""

import numpy as np
import re


file ='C:/Users/user/Documents/SOLPS data/simulation data/mast/g027205.00275.X2.equ'

with open(file) as f:
     datalist =f.readlines()

j= 17

while j< 43:
    string2 = datalist[j]
    gdata = re.findall('[-+]?\d+\.?\d+[eE]?[-+]\d+', string2)
    print(gdata)
    mylist =[]
    for ii in gdata:
        a = np.float64(ii) +np.float64(1.00000000)
        b = "{:.8E}".format(a)
        mylist.append(b)
    print(mylist)
    writelist = ' '.join(str(x)+"   " for x in mylist)
    datalist[j] = "\t" + writelist + "\n"
    print(datalist[j])
    j= j+ 1

with open(file,'w') as g:
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

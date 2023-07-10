# -*- coding: utf-8 -*-
"""
Created on Sun Jul  9 17:53:28 2023

@author: user
"""

import matplotlib.pyplot as plt
import B2TransportParser as b2tp
import tools as tl

one_list, n , filename_a, shift_a = tl.mast_tranco_dir('dot3')
print(one_list)
org_list = tl.mast_std_dir()

one_trans = b2tp.InputfileParser(one_list[0], plot= False)
ond = one_trans['1'].T
onki = one_trans['3'].T
onke = one_trans['4'].T
onx= ond[:,0]  #the coordinate here is R-R_sep
fd = ond[:,1]
fki = onki[:,1]
fke = onke[:,1]

dot3psi = tl.dsa_to_psi(onx)
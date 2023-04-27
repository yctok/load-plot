# -*- coding: utf-8 -*-
"""
Created on Mon Oct 10 22:19:16 2022

@author: user
"""

import matplotlib.pyplot as plt
from equilibrium import equilibrium
import B2TransportParser as b2tp


T_input = 'C:/Users/user/Documents/SOLPS data/simulation data/mast/b2.transport.inputfile'

trans_list = b2tp.InputfileParser(T_input, plot= False)
trans_co = trans_list['1']
x= trans_co[0,:]  #the coordinate here is R-R_sep

GF = 'C:/Users/user/Documents/SOLPS data/experiment data/MAST__RMP_results/g027205.00275_efitpp'

eq = equilibrium(gfile=GF)
R_sep = b2tp.PsiN2R(eq, 1.0)
new_R1 = []
for R1 in x:
        A = R1 + R_sep
        B = b2tp.R2PsiN(eq,A)
        new_R1.append(float(B))
x = new_R1


y= trans_co[1,:]

y[1] = 0.47796
y[2] = 0.44083
y[3] = 0.41751
y[13] = 0.09134
y[14] = 0.11463

st = trans_co[1,:]
stn = []
for cf in st:
    a = cf*1.2
    stn.append(a)

print(stn)

plt.plot(x,y, 'o-', color = 'orange', label ='Jameson_solution_original_setup')
plt.plot(x,stn, 'o-', color = 'red', label= 'Modify_one_meter_stable_solution')
plt.xlabel('Magnetic flux coordinate: ${\psi_N}$', fontdict={"family":"Times New Roman","size": 20})
plt.ylabel('Density-driven diffusivity: D (m$^{2}$/s)', fontdict={"family":"Times New Roman","size": 20})
plt.title('Density transport coefficient',fontdict={"family":"Times New Roman","size": 20})
plt.legend()



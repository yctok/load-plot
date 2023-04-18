# -*- coding: utf-8 -*-
"""
Created on Sun Oct  9 22:33:20 2022

@author: user
"""

import numpy as np
import matplotlib.pyplot as plt
import B2TransportParser as b2tp
from equilibrium import equilibrium


GF = 'C:/Users/user/Documents/SOLPS data/experiment data/mast/027205/g027205.00275_efitpp'

an_data_1 = 'C:/Users/user/Documents/SOLPS data/simulation data/mast/org/an3da.last10'
an_data_2 = 'C:/Users/user/Documents/SOLPS data/simulation data/mast/jameson/an3da.last10'
an_data_3 = 'C:/Users/user/Documents/SOLPS data/simulation data/mast/m1equ_stable/an3da.last10'

eq = equilibrium(gfile=GF)
Attempt1 = np.loadtxt(an_data_1)
Attempt2 = np.loadtxt(an_data_2)
Attempt3 = np.loadtxt(an_data_3)

#plt.plot(Attempt1[:,0], Attempt1[:,1])
#plt.plot(Attempt2[:,0], Attempt2[:,1])
#plt.show()

if len(Attempt1) != 0:
    Attempt1 = Attempt1.T
    R_sep = b2tp.PsiN2R(eq, 1.0)
    new_R1 = []
    for R1 in Attempt1[0]:
            A = R1 + R_sep
            B = b2tp.R2PsiN(eq,A)
            new_R1.append(float(B))
    Attempt1[0]=new_R1
    Attempt1 = Attempt1.T

#data_file = np.genfromtxt(ne_data ,delimiter='\t')

if len(Attempt2) != 0:
    Attempt2 = Attempt2.T
    R_sep = b2tp.PsiN2R(eq, 1.0)
    new_R2 = []
    for R2 in Attempt2[0]:
            A2 = R2 + R_sep
            B2 = b2tp.R2PsiN(eq,A2)
            new_R2.append(float(B2))
    Attempt2[0]=new_R2
    Attempt2 = Attempt2.T

if len(Attempt3) != 0:
    Attempt3 = Attempt3.T
    R3_sep = b2tp.PsiN2R(eq, 1.0)
    new_R3 = []
    for R3 in Attempt3[0]:
            A3 = R3 + R3_sep
            B3 = b2tp.R2PsiN(eq,A3)
            new_R3.append(float(B3))
    Attempt3[0]=new_R3
    Attempt3 = Attempt3.T

plt.yscale('log')
#plt.plot(new_R1, Attempt1[:,1], color = 'orange', label= 'original setup')
plt.plot(new_R2, Attempt2[:,1], color = 'green', label= 'Jameson_solution_original_setup')
plt.plot(new_R3, Attempt3[:,1], color = 'red', label= 'Modify_one_meter_stable_solution')
plt.xlabel('Magnetic flux coordinate: ${\psi_N}$', fontdict={"family":"Times New Roman","size": 20})
plt.ylabel('Neutral density: ${n_D}$ (m$^{-3}$)', fontdict={"family":"Times New Roman","size": 20})
plt.title('Neutral density',fontdict={"family":"Times New Roman","size": 20})
plt.legend()





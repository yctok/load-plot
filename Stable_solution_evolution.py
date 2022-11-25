# -*- coding: utf-8 -*-
"""
Created on Mon Oct 10 22:08:59 2022

@author: user
"""
import numpy as np
import matplotlib.pyplot as plt
import B2TransportParser as b2tp
from equilibrium import equilibrium



GF = 'C:/Users/user/Documents/SOLPS data/experiment data/MAST__RMP_results/g027205.00275_efitpp'

ne_data_1 = 'C:/Users/user/Documents/SOLPS data/simulation data/mast/mequ_stable1/an3da.last10'
ne_data_2 = 'C:/Users/user/Documents/SOLPS data/simulation data/mast/mequ_stable2/an3da.last10'
ne_data_3 = 'C:/Users/user/Documents/SOLPS data/simulation data/mast/mequ_stable3/an3da.last10'
ne_data_4 = 'C:/Users/user/Documents/SOLPS data/simulation data/mast/mequ_stable4/an3da.last10'

eq = equilibrium(gfile=GF)
Attempt1 = np.loadtxt(ne_data_1)
Attempt2 = np.loadtxt(ne_data_2)
Attempt3 = np.loadtxt(ne_data_3)
Attempt4 = np.loadtxt(ne_data_4)

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
    
if len(Attempt4) != 0:
    Attempt4 = Attempt4.T
    R4_sep = b2tp.PsiN2R(eq, 1.0)
    new_R4 = []
    for R4 in Attempt4[0]:
            A4 = R4 + R4_sep
            B4 = b2tp.R2PsiN(eq,A4)
            new_R4.append(float(B4))
    Attempt4[0]=new_R4
    Attempt4 = Attempt4.T



plt.plot(new_R1, Attempt1[:,1], color = 'orange')
plt.plot(new_R2, Attempt2[:,1], color = 'green')
plt.plot(new_R3, Attempt3[:,1], color = 'red')
plt.plot(new_R4, Attempt4[:,1], color = 'blue')
plt.xlabel('Magnetic flux coordinate: ${\psi_N}$', fontdict={"family":"Times New Roman","size": 20})
plt.ylabel('Electron density: ${n_e}$ (m$^{-3}$)', fontdict={"family":"Times New Roman","size": 20})
plt.title('Electron density',fontdict={"family":"Times New Roman","size": 20})
plt.show()
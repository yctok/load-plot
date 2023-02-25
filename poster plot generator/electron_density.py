# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import matplotlib.pyplot as plt
import B2TransportParser as b2tp
from equilibrium import equilibrium

exp_file = np.genfromtxt('C:/Users/user/Documents/SOLPS data/simulation data/mast/yag_27205_275.dat',delimiter=' ')

psi_n = []
exp_ne = []
err_ne =[]

j= 26

while j< 60:
    a = exp_file[j,0]
    psi_n.append(a)
    b = exp_file[j,2]
    exp_ne.append(b)
    c = exp_file[j,4]
    err_ne.append(c)
    j= j+ 1
    
#psi_n = exp_file[:,0]


plt.show()



GF = 'C:/Users/user/Documents/SOLPS data/experiment data/MAST__RMP_results/g027205.00275_efitpp'

ne_data_o = 'C:/Users/user/Documents/SOLPS data/simulation data/mast/org/ne3da.last10'
ne_data_m = 'C:/Users/user/Documents/SOLPS data/simulation data/mast/jameson/ne3da.last10'
ne_data_s = 'C:/Users/user/Documents/SOLPS data/simulation data/mast/m1equ_stable/ne3da.last10'


eq = equilibrium(gfile=GF)
Attempt1 = np.loadtxt(ne_data_o)
Attempt2 = np.loadtxt(ne_data_m)
Attempt3 = np.loadtxt(ne_data_s)

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

fig, ax = plt.subplots()
ax.errorbar(psi_n, exp_ne, err_ne, color = 'blue', label= 'experimental data')


#plt.plot(new_R1, Attempt1[:,1], color = 'orange', label= 'original setup')
plt.plot(new_R2, Attempt2[:,1], color = 'green', label= 'Jameson_solution_original_setup')
plt.plot(new_R3, Attempt3[:,1], color = 'red', label= 'Modify_one_meter_stable_solution')
plt.xlabel('Magnetic flux coordinate: ${\psi_N}$', fontdict={"family":"Times New Roman","size": 20})
plt.ylabel('Electron density: ${n_e}$ (m$^{-3}$)', fontdict={"family":"Times New Roman","size": 20})
plt.title('Electron density',fontdict={"family":"Times New Roman","size": 20})
plt.legend()










# -*- coding: utf-8 -*-
"""
Created on Sun Apr  2 12:58:02 2023

@author: user
"""

import numpy as np
import matplotlib.pyplot as plt
import B2TransportParser as b2tp
from equilibrium import equilibrium
from tools import set_wdir
import glob

dev = 'mast'
shot = '027205'
shift = 'org'
series = 'p4_d6'
a_list = []

basedrt, topdrt = set_wdir()

a_list = glob.glob('{}/{}/{}/{}/{}*'.format(basedrt, dev, shot, shift, series))
# print(a_list)
# print(len(a_list))
n_dir = len(a_list)

def number(text):
    name = text.split('\\',1)[1]
    nu = int(name.split('_')[2])

    return [nu, text]

print(number(a_list[0]))

a_list.sort(key=number)
print(a_list)

attempt_name = []

for j in range(n_dir):
    name = a_list[j]
    attempt_name.append(name.split('\\',1)[1])

print(attempt_name)



gtr = glob.glob('{}/{}/{}/g{}*'.format(topdrt, dev, shot, shot))
# print(gtr)

# GF = 'C:/Users/user/Documents/SOLPS data/experiment data/MAST__RMP_results/g027205.00275_efitpp'

# an_data_1 = 'C:/Users/user/Documents/SOLPS data/simulation data/mast/org/an3da.last10'
# an_data_2 = 'C:/Users/user/Documents/SOLPS data/simulation data/mast/jameson/an3da.last10'
# an_data_3 = 'C:/Users/user/Documents/SOLPS data/simulation data/mast/m1equ_stable/an3da.last10'

fd_list = []
last10_list = ['an3da.last10']


for i in range(n_dir):
    fd_list.append('{}/{}'.format(a_list[i], last10_list[0]))
    # print(fd_list[i])

# print(fd_list)


eq = equilibrium(gfile=gtr[-1])

data = {}

Attempt1 = np.loadtxt(fd_list[0])
Attempt1 = Attempt1.T




for k in range(n_dir):
    Attempt = np.loadtxt(fd_list[k])
    Attempt = Attempt.T
    R_sep = b2tp.PsiN2R(eq, 1.0)
    new_R = []
    for R in Attempt[0]:
            A = R + R_sep
            B = b2tp.R2PsiN(eq,A)
            new_R.append(float(B))
    Attempt[0]= new_R
    # Attempt = Attempt.T
    data[attempt_name[k]] = Attempt

# color_list = 

plt.figure(1)
for m in range(n_dir):
    plt.plot(data[attempt_name[m]][0], data[attempt_name[m]][1], label= attempt_name[m])

plt.xlabel('Magnetic flux coordinate: ${\psi_N}$', fontdict={"family":"Times New Roman","size": 20})
plt.ylabel('Neutral density: ${n_D}$ (m$^{-3}$)', fontdict={"family":"Times New Roman","size": 20})
plt.title('Neutral density',fontdict={"family":"Times New Roman","size": 20})
plt.legend()









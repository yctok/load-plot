# -*- coding: utf-8 -*-
"""
Created on Mon Apr  3 03:19:47 2023

@author: user
"""

psi_solps =[0.56591402, 0.59635553, 0.65365526, 0.70507622, 0.75083496,
        0.79132874, 0.82698182, 0.85806206, 0.88490369, 0.90789432,
        0.92738632, 0.94367313, 0.95706941, 0.96795829, 0.97677538,
        0.9838775 , 0.98955578, 0.99415907, 0.99803803, 1.002408  ,
        1.00753157, 1.01263476, 1.01772166, 1.02279374, 1.02785249,
        1.03288158, 1.03794617, 1.04306613, 1.04817989, 1.05328886,
        1.05838546, 1.06347049, 1.06855367, 1.07363646, 1.07872032,
        1.08380671, 1.08889011, 1.09145489]

import numpy as np
import matplotlib.pyplot as plt
import B2TransportParser as b2tp
from equilibrium import equilibrium
import tools as tl
import glob

dev = 'mast'
shot = '027205'
shift = 'org'
series = ['try & error','p4_d6_9']
s_choose = 1

a_list = []
# b_list = []
basedrt, topdrt = tl.set_wdir()

if s_choose == 0:
    a_list = glob.glob('{}/{}/{}/{}/{}/p4_*'.format(basedrt, dev, shot, shift, series[0]))
elif s_choose == 1:
    a_list = glob.glob('{}/{}/{}/{}/{}*'.format(basedrt, dev, shot, shift, series[1]))
    

a_list.sort(key=tl.a_number)


n_dir = len(a_list)

attempt_name = []

for j in range(n_dir):
    name = a_list[j]
    attempt_name.append(name.split('\\',1)[1])

print(attempt_name)


gtr = glob.glob('{}/{}/{}/g{}*'.format(topdrt, dev, shot, shot))
print(gtr)

fd_list = []
last10_list = ['ne3da.last10']
fd_dic = {}


for jj in last10_list:
    fd_list = []
    for i in range(n_dir):
        fd_list.append('{}/{}'.format(a_list[i], jj))
    fd_dic[jj] = fd_list
    # print(fd_list[i])


eq = equilibrium(gfile=gtr[-1])
data2 = {}

Attempt1 = np.loadtxt(fd_list[0])
Attempt1 = Attempt1.T
R_sep = b2tp.PsiN2R(eq, 1.0)
R_file = []
for R in Attempt1[0]:
        A = R + R_sep
        R_file.append(float(A))
Attempt1[0]= R_file


# instance = SOLPSxport(workdir= a_list[-1], gfile_loc = gtr[-1], impurity_list=[])
# instance.calcPsiVals(plotit = False, dsa = None, b2mn = None, geo = None, verbose=True, shift=0)


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
    data2[attempt_name[k]] = Attempt
    
plt.figure(1)
plt.scatter(R_file, data2[attempt_name[0]][0], label= attempt_name[0])
plt.scatter(R_file, psi_solps, label= attempt_name[0])

plt.show()

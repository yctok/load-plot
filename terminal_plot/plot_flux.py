# -*- coding: utf-8 -*-
"""
Created on Fri Apr 14 15:15:51 2023

@author: user
"""

import SOLPSutils as sut
import matplotlib.pyplot as plt




xa, f0 = sut.B2pl("fnay za m* 0 0 sumz sy m/ writ jxa f.y")
xb, qe0 = sut.B2pl("fhey sy m/ writ jxa f.y")
xc, qi0 = sut.B2pl("fhiy sy m/ writ jxa f.y")
xd, ptheta = sut.B2pl("fnax za m* 0 0 sumz sx m/ writ jxa f.y")


plt.figure(1)
plt.scatter(xa, f0, label= 'electron temperature experiment data')
plt.xlabel('Radial coordinate: $R- R_{sep}$', fontdict={"family":"Times New Roman","size": 20})
plt.ylabel('particle flux', fontdict={"family":"Times New Roman","size": 20})
plt.title('particle flux',fontdict={"family":"Times New Roman","size": 20})
plt.legend()

plt.figure(2)
plt.scatter(xb, qe0, label= 'electron temperature experiment data')
plt.xlabel('Radial coordinate: $R- R_{sep}$', fontdict={"family":"Times New Roman","size": 20})
plt.ylabel('electron heat flux', fontdict={"family":"Times New Roman","size": 20})
plt.title('electron heat flux',fontdict={"family":"Times New Roman","size": 20})
plt.legend()

plt.figure(3)
plt.scatter(xc, qi0, label= 'electron temperature experiment data')
plt.xlabel('Radial coordinate: $R- R_{sep}$', fontdict={"family":"Times New Roman","size": 20})
plt.ylabel('ion heat flux', fontdict={"family":"Times New Roman","size": 20})
plt.title('ion heat flux',fontdict={"family":"Times New Roman","size": 20})
plt.legend()

plt.figure(4)
plt.scatter(xd, ptheta, label= 'electron temperature experiment data')
plt.xlabel('Radial coordinate: $R- R_{sep}$', fontdict={"family":"Times New Roman","size": 20})
plt.ylabel('poloidal flux', fontdict={"family":"Times New Roman","size": 20})
plt.title('poloidal flux',fontdict={"family":"Times New Roman","size": 20})
plt.legend()



plt.show()

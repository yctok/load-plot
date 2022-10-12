# -*- coding: utf-8 -*-
"""
Created on Mon Oct 10 22:19:16 2022

@author: user
"""

import re
import matplotlib.pyplot as plt
import numpy as np
import equilibrium
import B2TransportParser as btp

T_input = 'C:/Users/user/Documents/SOLPS data/simulation data/mast/b2.transport.inputfile'

trans_list = btp.InputfileParser(T_input, plot= True)


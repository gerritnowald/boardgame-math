# -*- coding: utf-8 -*-
"""
Created on Sun Apr  3 13:11:29 2022

@author: Gerrit Nowald
"""

import itertools
import numpy as np
from matplotlib import pyplot as plt

#------------------------------------------------------------------------------
# input

dices = [6,6]

# dices = [2,2,2]

#------------------------------------------------------------------------------
# calculation

eyes = []
for dice in dices:
    eyes.append( [eye+1 for eye in range(dice)] )

combinations = list(itertools.product(*eyes))

eyesum = []
for combination in combinations:
    eyesum.append(sum(combination))

plt.hist(eyesum, bins=np.arange(min(eyesum)-3,len(set(eyesum))+2)+1.5, density=True, rwidth=0.9)
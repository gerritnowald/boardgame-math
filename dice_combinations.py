# -*- coding: utf-8 -*-
"""
Created on Sun Apr  3 13:11:29 2022

@author: Gerrit Nowald
"""

import itertools
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.ticker import MaxNLocator

#------------------------------------------------------------------------------
# input

dices = [6,6,20]

#------------------------------------------------------------------------------
# calculation

eyes = []
for dice in dices:
    eyes.append( [eye+1 for eye in range(dice)] )

combinations = list(itertools.product(*eyes))

eyesum = []
for combination in combinations:
    eyesum.append(sum(combination))

#------------------------------------------------------------------------------
# plot

ax = plt.figure().gca()
plt.hist(eyesum, bins=np.arange( min(eyesum), min(eyesum)+len(set(eyesum))+1, 1 ) - 0.5, density=True, rwidth=0.8)
plt.title('probabilities of eyesums')
plt.xlabel('eye sum')
plt.ylabel('probability')
ax.xaxis.set_major_locator(MaxNLocator(integer=True))
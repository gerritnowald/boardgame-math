# -*- coding: utf-8 -*-
"""
plots the probability distribution of 
the eye sum of arbitrary many, arbitrary sided die

Created on Sun Apr  3 13:11:29 2022

@author: Gerrit Nowald
"""

import itertools
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.ticker import MaxNLocator

#------------------------------------------------------------------------------
# input

# list of die; e.g. [6,6,20]: two 6-sided die, one 20-sided dice
die = [6,6,20]

#------------------------------------------------------------------------------
# calculation

# list of lists of all possible eyes for each dice
eyes = []
for dice in die:
    eyes.append( [eye+1 for eye in range(dice)] )

# all possible result combinations
combinations = list(itertools.product(*eyes))

# sum of eyes for each combination
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
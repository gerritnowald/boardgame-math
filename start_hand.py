# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 19:08:27 2022

gives the propability to have at least 1 card in the start hand

@author: Gerrit Nowald
"""

#------------------------------------------------------------------------------
# input

Deck  = 60
Hand  = 7
Cards = 4

#------------------------------------------------------------------------------
# calculation

p = 1
for n in range(0,Hand):
    p *= (Deck-Cards-n)/(Deck-n)    # chance to have no card in hand
p = 1 - p   # counter propability

#------------------------------------------------------------------------------
# output

print(f'{round(p*100)} % chance to have at least 1 card in the start hand')
# -*- coding: utf-8 -*-
"""
gives the propability to have at least 1 certain card in the start hand

Created on Fri Mar 11 19:08:27 2022

@author: Gerrit Nowald
"""

#------------------------------------------------------------------------------
# input

Deck  = 60  # total cards in deck
Hand  = 7   # cards in start hand
Cards = 4   # total number of certain card in deck

#------------------------------------------------------------------------------
# calculation

p = 1
for n in range(0,Hand):
    p *= (Deck-Cards-n)/(Deck-n)    # chance to have none of the certain card in hand
p = 1 - p                           # counter propability

#------------------------------------------------------------------------------
# output

print(f'{round(p*100)} % chance to have at least 1 card in the start hand')
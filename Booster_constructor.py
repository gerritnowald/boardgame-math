# -*- coding: utf-8 -*-
"""
Calculates how many booster packs can be build based on available cards for each rarity
and gives how many cards of each rarity are missing to build additional booster.

Based on the number of rares, uncommons & commons, it is calculated how many booster can be build right now, based on the given ratios between the three rarities. 
Standard Magic: The Gathering draft booster contain 1 rare, 3 uncommon and 10 common cards 
(Additionally, they also contain 1 standard land and either a token or a promotional card). 
Then, it is calculated what minimum addition of cards is needed in order to use all cards of at least one rarity, until all cards are used.

Created on Mon Sep 27 14:32:51 2021

@author: Gerrit Nowald
"""

import numpy as np

#------------------------------------------------------------------------------
# input

cards = np.array([0, 44, 51])     # my Kaldheim cards
# cards = np.array([0, 26, 17])     # my Eldraine cards
# cards = np.array([8, 13, 8])      # my Theros cards
# cards = np.array([8, 83, 76])     # all together

# test
# cards = np.array([3, 0, 31])
# cards = np.array([3, 31, 31])
# cards = np.array([3, 30, 31])
# cards = np.array([3, 9, 30])

print(f"Cards available: {cards[0]}xR, {cards[1]}xU, {cards[2]}xC")
print("")

#------------------------------------------------------------------------------
# defintions

ratios = np.array([1, 3, 10])    # number rare, uncommon & common per booster

#------------------------------------------------------------------------------
# calculation

while max(cards) > 0:
    possible = cards // ratios
    try:
        booster = min(possible[possible>0])     # raises error when all entries in possible are zero
        buy  = booster*ratios - cards
        buy[buy<0] = 0
        cards += buy - booster*ratios
        if np.all(cards < ratios) and max(cards) > 0:   # last booster
            booster += 1
            buy  += ratios - cards
            cards += buy - booster*ratios
        if max(buy) == 0:
            print(f"{booster} booster can be build directly.")
        else:
            print(f"With additional  {buy[0]}xR, {buy[1]}xU, {buy[2]}xC,  additional {booster} booster can be build.")
        if max(cards) > 0:
            print(f"Cards left:      {cards[0]}xR, {cards[1]}xU, {cards[2]}xC")
        else:
            print("All cards used.")
        print("")
    except:
        break

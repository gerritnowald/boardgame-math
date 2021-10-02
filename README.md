# MTG_booster_constructor
A simple Python script to calculate how many MTG booster can be build and how many cards of each rarity are missing to build additional booster.

Based on the number of rares, uncommons & commons, it is calculated how many booster can be build right now, based on the given ratios between the three rarities.
Standard draft booster contain 1 rare, 3 uncommon and 10 common cards (Additionally, they also contain 1 standard land and either a token or a promotional card).
Then, it is calculated what minimum addition of cards is needed in order to use all cards of at least one rarity, until all cards are used.

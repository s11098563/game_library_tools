# Dice Rolling Library, Connor Cook, Feb 18, 2021, 1:59PM v0.2

import random

# d4 simulator
def roll_d4(num_roll): # num_roll is an arguement
    rolls = 0
    sum = 0

    while rolls < num_roll:
        result = random.randint(1, 4)
        print(f"You have rolled a {result}.\n")
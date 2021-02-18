# Dice Rolling Library, Connor Cook, Feb 18, 2021, 2:04PM v0.3

import random

# d4 simulator
def roll_d4(num_roll): # num_roll is an arguement
    rolls = 0
    sum = 0

    while rolls < num_roll:
        result = random.randint(1, 4)
        print(f"You have rolled a {result}.\n")
        rolls += 1
        sum += result
    
    print(f"The sum of all your rolls is {sum}.\n")


roll_d4()
# Dice Rolling Library, Connor Cook, Feb 18, 2021, 2:23PM v0.4.5

import random
import time

# d4 simulator
def roll_d4(num_roll): # num_roll is an arguement
    rolls = 0
    sum = 0

    while rolls < num_roll:
        result = random.randint(1, 4)
        print(f"You have rolled a {result}.\n")
        time.sleep(1)
        rolls += 1
        sum += result
    
    print(f"The sum of all your rolls is {sum}.\n")



# d6 simulator
def roll_d6(num_roll): # num_roll is an arguement
    rolls = 0
    sum = 0

    while rolls < num_roll:
        result = random.randint(1, 6)
        print(f"You have rolled a {result}.\n")
        time.sleep(1)
        rolls += 1
        sum += result
    
    print(f"The sum of all your rolls is {sum}.\n")



# d8 simulator
def roll_d8(num_roll): # num_roll is an arguement
    rolls = 0
    sum = 0

    while rolls < num_roll:
        result = random.randint(1, 8)
        print(f"You have rolled a {result}.\n")
        time.sleep(1)
        rolls += 1
        sum += result
    
    print(f"The sum of all your rolls is {sum}.\n")



# d10 simulator
def roll_d10(num_roll): # num_roll is an arguement
    rolls = 0
    sum = 0

    while rolls < num_roll:
        result = random.randint(1, 10)
        print(f"You have rolled a {result}.\n")
        time.sleep(1)
        rolls += 1
        sum += result
    
    print(f"The sum of all your rolls is {sum}.\n")



# d12 simulator
def roll_d12(num_roll): # num_roll is an arguement
    rolls = 0
    sum = 0

    while rolls < num_roll:
        result = random.randint(1, 12)
        print(f"You have rolled a {result}.\n")
        time.sleep(1)
        rolls += 1
        sum += result
    
    print(f"The sum of all your rolls is {sum}.\n")



# d20 simulator
def roll_d20(num_roll): # num_roll is an arguement
    rolls = 0
    sum = 0

    while rolls < num_roll:
        result = random.randint(1, 20)
        print(f"You have rolled a {result}.\n")
        time.sleep(1)
        rolls += 1
        sum += result
    
    print(f"The sum of all your rolls is {sum}.\n")



# d100 simulator
def roll_d100(num_roll): # num_roll is an arguement
    rolls = 0
    sum = 0

    while rolls < num_roll:
        result = random.randint(1, 100)
        print(f"You have rolled a {result}.\n")
        time.sleep(1)
        rolls += 1
        sum += result
    
    print(f"The sum of all your rolls is {sum}.\n")



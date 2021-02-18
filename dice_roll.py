# Dice Rolling Library, Connor Cook, Feb 18, 2021, 2:16PM v0.4

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


# roll_d4()


# d6 simulator
def roll_d6(num_roll): # num_roll is an arguement
    rolls = 0
    sum = 0

    while rolls < num_roll:
        result = random.randint(1, 6)
        print(f"You have rolled a {result}.\n")
        rolls += 1
        sum += result
    
    print(f"The sum of all your rolls is {sum}.\n")


# roll_d6()


# d8 simulator
def roll_d8(num_roll): # num_roll is an arguement
    rolls = 0
    sum = 0

    while rolls < num_roll:
        result = random.randint(1, 8)
        print(f"You have rolled a {result}.\n")
        rolls += 1
        sum += result
    
    print(f"The sum of all your rolls is {sum}.\n")


# roll_d8()


# d10 simulator
def roll_d10(num_roll): # num_roll is an arguement
    rolls = 0
    sum = 0

    while rolls < num_roll:
        result = random.randint(1, 10)
        print(f"You have rolled a {result}.\n")
        rolls += 1
        sum += result
    
    print(f"The sum of all your rolls is {sum}.\n")


# roll_d10


# d12 simulator
def roll_d12(num_roll): # num_roll is an arguement
    rolls = 0
    sum = 0

    while rolls < num_roll:
        result = random.randint(1, 12)
        print(f"You have rolled a {result}.\n")
        rolls += 1
        sum += result
    
    print(f"The sum of all your rolls is {sum}.\n")


# roll_d12()


# d20 simulator
def roll_d20(num_roll): # num_roll is an arguement
    rolls = 0
    sum = 0

    while rolls < num_roll:
        result = random.randint(1, 20)
        print(f"You have rolled a {result}.\n")
        rolls += 1
        sum += result
    
    print(f"The sum of all your rolls is {sum}.\n")


# roll_d20


# d100 simulator
def roll_d100(num_roll): # num_roll is an arguement
    rolls = 0
    sum = 0

    while rolls < num_roll:
        result = random.randint(1, 100)
        print(f"You have rolled a {result}.\n")
        rolls += 1
        sum += result
    
    print(f"The sum of all your rolls is {sum}.\n")


# roll_d100


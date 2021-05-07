#! /usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  7 11:28:47 2021

@author: Bea Jimenez <bea.jimenez@alumni.ie.edu>
"""

"""
Pick a first random number between 1 and 20
Pick a first random number between 1 and 10
Show the addition and the floor division between both numbers
While the player hasn’t guessed both numbers, let the player guess
Congratulate the player when he guesses both numbers
"""

import random

firstRand = random.randint(1,20)
secondRand = random.randint(1,20)

addition = firstRand + secondRand
floorDivision = firstRand / secondRand

guessedNumber = 0

while  guessedNumber != randomNumber:

    guessedNumber = int(input('Guess the nummber\n'))

    if guessedNumber < randomNumber:
        print('higher! keep trying')
    else: 
        print('lower! keep trying')        
        
print('congrats!')

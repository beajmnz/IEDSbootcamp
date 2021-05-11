#! /usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  5 13:38:47 2021

@author: Bea Jimenez <bea.jimenez@alumni.ie.edu>
"""

"""
Pick a random number between 1 and 20
While the player hasn’t guessed the number, let the player guess
Congratulate the player when he guesses the number
Tip: use the randint(x,y) function from the module “random“ to create a random
number .
To import the module and to use the command you have to write:
import random # to import the module
random.randint(1,6) # to create a random integer between 1 and 6
"""

import random

randomNumber = random.randint(1,20)
guessedNumber = 0

while  guessedNumber != randomNumber:

    guessedNumber = int(input('Guess the nummber\n'))

    if guessedNumber < randomNumber:
        print('higher! keep trying')
    else: 
        print('lower! keep trying')        
        
print('congrats!')

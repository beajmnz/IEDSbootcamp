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
floorDivision = firstRand // secondRand

print("I have thought of two numbers. Their sum is",addition,
      "and their floor division is",floorDivision,"\n.")

guessedNumber1 = int(input('Guess the first nummber\n'))
guessedNumber2 = int(input('Guess the second nummber\n'))

while  (guessedNumber1 != firstRand) and (guessedNumber2 != secondRand):

    guessedNumber1 = int(input('Nice try! Guess the first nummber\n'))
    guessedNumber2 = int(input('Guess the second nummber\n'))

        
print('congrats!')

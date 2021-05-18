#! /usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 18 17:16:20 2021

@author: Bea Jimenez <bea.jimenez@alumni.ie.edu>
"""

"""
Guess the number
================

The player is asked to guess a number between 1 and 100, picked randomly by the program.
Each time they propose an answer, the program tells them if their answer is correct, too low, or too high.
The player has an unlimited number of attempts (or, in a variant, a limited number of attempts).
"""

import random

nr2Bguessed = random.randint(1, 100)

attempt = int(
    input(
        "I have thought of a number between 1 and 100. Try and guess it!\nGive a number\n"
    )
)

while attempt != nr2Bguessed:
    if attempt < nr2Bguessed:
        attempt = int(input("Too low. Guess again\n"))
    else:
        attempt = int(input("Too high. Guess again\n"))

print("You did it!")

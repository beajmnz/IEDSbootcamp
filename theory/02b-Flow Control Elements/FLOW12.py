#! /usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 10 19:24:53 2021

@author: Bea Jimenez <bea.jimenez@alumni.ie.edu>
"""

"""
Write a Python program that accepts a string and calculate the number
of digits and letters
Tip: check this:
a = "2"              b="t"
a.isdigit()          b.isdigit()
a.isalpha()          b.isalpha()
"""

string2calculate = input("Write a password-like string with mixed digits and letters\n")

digits = 0
letters = 0
other = 0

for character in string2calculate:
    if character.isdigit():
        digits += 1
    elif character.isalpha():
        letters += 1
    else:
        other += 1
        
print("Your string had",digits,"digits,",letters,"letters and ",other,"other characters.")

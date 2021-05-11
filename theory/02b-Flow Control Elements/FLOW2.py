#! /usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  5 12:52:51 2021

@author: Bea Jimenez <bea.jimenez@alumni.ie.edu>
"""

"""
Write a Python program that receives a number and shows one of these
options:
- The number is negative
- The number is 0
- The number is in [10,20]
- The number is in (0,10) or bigger than 20
"""

number = int(input("Enter an integer number\n"))

if number < 0 :
    print("the number",number,"is negative")
elif number == 0 :
    print("the number",number,"is 0")
elif number >10 and number <= 20:
    print("the number",number,"is in [10,20]")
elif (number >0 and number <10) or number > 20:
    print("the number",number,"is in (0,10) or >20")
else:
    print('are you sure you put a number there?')
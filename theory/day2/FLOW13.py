#! /usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 10 19:34:00 2021

@author: Bea Jimenez <bea.jimenez@alumni.ie.edu>
"""

"""
Write a Python program to calculate a dog's age in human's years. The
program receives the dog's age and shows the equivalent human's
age.
Note: For each of the first two years, a dog year is equal to 10.5 human
years. After that, each dog year is equal to 4 human years.
"""

dogsAge = float(input("Enter a dog's age\n"))

if dogsAge <= 2:
    print("The equivalent in human years is",dogsAge*10.5)
else:
    print("The equivalent in human years is",dogsAge*4)
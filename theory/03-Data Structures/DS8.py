#! /usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 11 09:09:24 2021

@author: Bea Jimenez <bea.jimenez@alumni.ie.edu>
"""

"""
Write a Python program to find maximum and the minimum value in a set.
"""


values = {16,2,3,45,5,6,72,8,9}


maxValue = values.pop()
minValue = maxValue

# OPTION 1

while len(values) > 0:
    i = values.pop()  # It's not a good idea to  modify the iterable within a loop
    if i > maxValue: maxValue = i
    if i < minValue: minValue = i
    
# OPTION 2

for value in values:
    if value > maxValue: maxValue = value
    if value < minValue: minValue = value


    
print("Max:",maxValue,"\nMin:",minValue)
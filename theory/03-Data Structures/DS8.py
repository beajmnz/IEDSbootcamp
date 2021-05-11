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

while len(values) > 0:
    i = values.pop()
    if i > maxValue: maxValue = i
    if i < minValue: minValue = i
    
print("Max:",maxValue,"\nMin:",minValue)


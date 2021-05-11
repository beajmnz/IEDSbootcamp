#! /usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  5 18:24:27 2021

@author: Bea Jimenez <bea.jimenez@alumni.ie.edu>
"""

"""
Write a Python program to count the elements in a list until an element
is a tuple.
Input:  [10,20,30,(10,20),40]
Output: 3
"""

Input =  [10,20,30,(10,20),40]
counter = 0

for i in Input:
    if type(i) != tuple:
        counter+=1
    else:
        break
    
print("There were",counter,"elements before the first tuple")
        
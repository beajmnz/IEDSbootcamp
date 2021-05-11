#! /usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 11 09:15:20 2021

@author: Bea Jimenez <bea.jimenez@alumni.ie.edu>
"""

"""
Write a Python program to remove a concrete item from a set if it is
present in the set.
"""

values = {16,2,3,45,5,6,72,8,9}

while len(values) > 0:
    print(values)
    value2remove = int(input("Write the value to be removed\n"))    
    if value2remove in values: values.pop()


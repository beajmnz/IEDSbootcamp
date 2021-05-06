#! /usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  6 12:49:44 2021

@author: Bea Jimenez <bea.jimenez@alumni.ie.edu>
"""

"""
Define a function where 2 numbers are given and it returns the addition
if both are lower than 10 and the product in other case.
"""

def weirdFunction(x,y):
    if x<10 and y<10:
        return x+y
    else:
        return x*y
    
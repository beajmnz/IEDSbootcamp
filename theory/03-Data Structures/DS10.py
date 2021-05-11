#! /usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  5 18:53:54 2021

@author: Bea Jimenez <bea.jimenez@alumni.ie.edu>
"""

"""
Write a Python program to do (A U B) ∩ C and the result has to be
composed by only 2 elements
"""

setA = {1,2,3,4}
setB = {5,6,7,8}
setC = {2,7}

solution = (setA | setB)  & setC

print(solution)
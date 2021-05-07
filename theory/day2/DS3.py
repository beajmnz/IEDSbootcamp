#! /usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  7 12:16:11 2021

@author: Bea Jimenez <bea.jimenez@alumni.ie.edu>
"""

"""
Write a Python program to split a list every n element
Inputs: ["a","b","c","d","e","f","g"]
n=3
Output: ["a","d","g"],["b","e"],["c","f"]
"""

Inputs = ["a","b","c","d","e","f","g"]
n = 3
Output = []

for i in range(n):
    Output.append(Inputs[i::n])

print(Output)

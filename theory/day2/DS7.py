#! /usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  5 18:26:56 2021

@author: Bea Jimenez <bea.jimenez@alumni.ie.edu>
"""

"""
Write a Python program to convert a tuple to a string.
Input: ("e","x","e","r","c","i","c","e","s")
Output: ""exercises
"""

Input = ("e","x","e","r","c","i","c","e","s")
Output = ""

for i in range(len(Input)):
    Output += Input[i]
    
print(Output)
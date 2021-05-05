#! /usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  5 18:29:19 2021

@author: Bea Jimenez <bea.jimenez@alumni.ie.edu>
"""

"""
Write a Python program to reverse a tuple.
"""

Input = ("e","x","e","r","c","i","c","e","s")
Output = ""

Output = list(Input)
Output.reverse()
Output = tuple(Output)
    
print(Output)
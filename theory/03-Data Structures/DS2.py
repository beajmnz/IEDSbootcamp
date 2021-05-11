#! /usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  7 12:16:11 2021

@author: Bea Jimenez <bea.jimenez@alumni.ie.edu>
"""

"""
Write a Python program to remove duplicated values from a list
Input: [1,2,3,2,2,2,1,5,5,7,8,9]
Output: [1,2,3,5,7,8,9]
"""

Input = [1,2,3,2,2,2,1,5,5,7,8,9]
Output = [] 

for i in Input:
    if i not in Output:
        Output.append(i)
print(Output)

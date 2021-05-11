#! /usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 11 09:07:02 2021

@author: Bea Jimenez <bea.jimenez@alumni.ie.edu>
"""

"""
Write a Python program which multiplies all the items in a list
"""

list2multiply = [1,2,3,2,2,2,1,5,5,7,8,9]

output = 1

for i in list2multiply:
    output = output * i
    
print(output)
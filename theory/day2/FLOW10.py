#! /usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  5 16:02:28 2021

@author: Bea Jimenez <bea.jimenez@alumni.ie.edu>
"""

"""
Write a Python program to get the Fibonacci series between 0 and 100
Expected output: 1, 1, 2, 3, 5, 8, 13...
"""
a = 0
b = 1
for i in range(100):
     print(a, end=',')
     c = a + b
     a = b
     b = c
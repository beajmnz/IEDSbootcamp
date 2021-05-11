#! /usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 11 10:13:29 2021

@author: Bea Jimenez <bea.jimenez@alumni.ie.edu>
"""

"""
Write a Python script to generate and print a dictionary that contains a
number (between 1 and n) in the form (x, x*x)
Tip: n=5. Expected output: {1:1, 2:4, 3:9, 4:16, 5:25}
"""

length = int(input("Enter the dictionary length\n"))

dictOfSquares = dict()

for i in range(1,length+1):
    dictOfSquares[i] = i*i
    
print(dictOfSquares)
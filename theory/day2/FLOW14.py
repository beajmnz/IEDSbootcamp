#! /usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  5 16:07:04 2021

@author: Bea Jimenez <bea.jimenez@alumni.ie.edu>
"""

"""
Write a Python program which asks for a number to the user and
shows the multiplication table for that value
Expected input: 9 Expected output
9x0=0 
9x1=9 
9x2=18 
...
9x10=90
"""

number2multipy = int(input('Say a number and I\'ll create the multiplication table\n'))

for i in range(11):
    print(number2multipy,'x',i,'=',number2multipy*i)
    
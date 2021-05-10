#! /usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  6 12:25:36 2021

@author: Bea Jimenez <bea.jimenez@alumni.ie.edu>
"""

"""
Write a Python program to get as output an arrow as follows:
+
++
+++
++++
+++++
++++
+++
++
+
Tip:
you can concatenate a couple of ranges with command chain from itertools library:
# Example:
itertools.chain(range(5),range(10)) is a vector with values 0, 1, 2, …4, 0, 1, 2, … 9
"""

height = int(input("Enter the height in lines you desire for the arrow\n"))

width = height // 2
    
# OPTION 1    

for i in range(1,height+1):
    if i <= width:
        print("+"*i)
    else:
        print("+"*(height-i+1))
        
        
## OPTION 2

import itertools

if (height % 2 != 0):
    for i in itertools.chain(range(width),range(width,0,-1)):
        print("+"*i)
else: 
    for i in itertools.chain(range(width+1),range(width,0,-1)):
        print("+"*i)


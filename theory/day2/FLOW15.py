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

height = 15

for i in range(1,height):
    if(i < height/2):
        print("*"*i)
    else:
        print("*"*(height-i))
        
        
## OPTION 2

import itertools


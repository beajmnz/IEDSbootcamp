#! /usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  5 17:31:21 2021

@author: Bea Jimenez <bea.jimenez@alumni.ie.edu>
"""

"""
Write a Python program to check if it has or not some negative value in
a given list. Output:
There is (or there is not) negative values.
"""

list1 = [1,2,3,2,2,2,1,5,5,7,8,9]
negativeFound = False

for i in list1:
    if i < 0:
        print("There are negative values")
        negativeFound = True
        break

if not negativeFound:
    print("There are no negative values")    

################################
##  SECOND SOLUTION
################################

list1.sort()
if list1[0] < 0:
    print("There are negative values")
else:
    print("There are no negative values")  
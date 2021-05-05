#! /usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  5 15:58:33 2021

@author: Bea Jimenez <bea.jimenez@alumni.ie.edu>
"""

"""
Write a Python program to remove the characters which have odd
index values of a given string.
Example: "this exercise is easy" Expected output: "ti xriei ay"
"""

givenString = input('type any string and I\'ll remove the odd characters\n')

print(givenString[::2])
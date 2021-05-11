#! /usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  5 16:31:11 2021

@author: Bea Jimenez <bea.jimenez@alumni.ie.edu>
"""

"""
Write a Python program to reverse words in a string.

Tip: check this example:
string = "My name is Pablo" Expected output: "yM eman si olbaP"
"""

givenString = input('type any string and I\'ll reverse the words\n')

splitString = givenString.split(' ')
endString = ''
for i in splitString:
    endString += i[::-1]
    endString += ' '
    
print(endString.strip())
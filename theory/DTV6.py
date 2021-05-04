#! /usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  4 17:07:54 2021

@author: Bea Jimenez <bea.jimenez@alumni.ie.edu>
"""

"""
Write a Python program to lowercase only the first 6 characters in a string.
Example:
Sample string: "STreeT Maria de Molina"
Expected result: "street Maria de Molina"
"""

sampleString = "STreeT Maria de Molina"

expectedResult = sampleString[:6].lower()+sampleString[6:]
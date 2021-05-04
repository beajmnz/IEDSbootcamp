#! /usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  4 17:20:35 2021

@author: Bea Jimenez <bea.jimenez@alumni.ie.edu>
"""

"""
Write a Python program to replace the first letter by $ in the remaining text.
Example:
Sample String : 'restart'
Expected Result : 'resta$t'
"""

sampleString = 'restart'
expectedResult = sampleString[0]+sampleString[1:].replace(sampleString[0],'$')
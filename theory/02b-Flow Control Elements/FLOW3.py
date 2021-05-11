#! /usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  5 13:03:37 2021

@author: Bea Jimenez <bea.jimenez@alumni.ie.edu>
"""

"""
Write a Python program that asks for a name to the user. If that name is your
name, give congratulations. If not, let him know that is not your name
Mark: be careful because the given text can have uppercase or lowercase
letters
"""

name = input('Guess my name').strip().lower()

if name == 'bea':
    print('congrats!')
else:
    print('too bad')
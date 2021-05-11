#! /usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  5 12:35:02 2021

@author: Bea Jimenez <bea.jimenez@alumni.ie.edu>
"""

# Write a Python program that receives a number and shows if it is multiple of
#5 or not

number = int(input("Enter an integer number\n"))

if number % 5 == 0 :
    print("the number",number,"is a multiple of five")
else :
    print("the number",number,"is not a multiple of five")
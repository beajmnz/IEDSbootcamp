#! /usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  4 17:37:20 2021

@author: Bea Jimenez <bea.jimenez@alumni.ie.edu>
"""

"""
Ask for a number and for a text. Write a program that prints the text the
number of times specified
"""

text = input("please write some text: ")
text = text + "\n" # we add a break line character 
number = int(input("please input the number of times to write the text: "))

repeatedText = text*number

print(repeatedText)
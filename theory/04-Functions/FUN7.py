#! /usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  6 12:49:44 2021

@author: Bea Jimenez <bea.jimenez@alumni.ie.edu>
"""

"""
Write a Python program that accepts a hyphen separated sequence of
words as input and prints the words in a hyphen separated sequence
after sorting them alphabetically.
"""

sentence = input("Type a hyphen separated sequence of words")

words = sentence.split("-")
words.sort()
output = "-".join(words)


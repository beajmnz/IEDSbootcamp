#! /usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 10 19:11:22 2021

@author: Bea Jimenez <bea.jimenez@alumni.ie.edu>
"""

"""
Write names until you give one of the objects in the picture.
Mark: use a expression similar to the following one:
vble in [“objectA”,”objectB”,”objectC”,”objectD”]
will return:
True if vble takes one of these values “objectA”, …, “objectD”
False if vble does not take the value “objectA”, …, “objectD”
"""

objects = ["shirt","blazer","diamond","high heels","necklace","sockets" ]

guessedObject = input('Give the name of an object\n')

while guessedObject not in objects:
    guessedObject = input("Give another object\n")
    
print("You did it!")
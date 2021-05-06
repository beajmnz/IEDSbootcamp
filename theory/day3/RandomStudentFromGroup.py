#! /usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  6 13:04:54 2021

@author: Bea Jimenez <bea.jimenez@alumni.ie.edu>
"""

"""
Create a function that, given a name of a group, returns a random student 
within the group
"""

import random


def studentFromGroup(group):

    groups = {"groupA":("Bea","Andrea","Andres"),
              "groupB":("Gabriella","Karla","Bianca"),
              "groupC":("Dario","Sebastian","Marielvic")}
    
    return random.choice(groups[group])

print(studentFromGroup("groupA"))
print(studentFromGroup("groupB"))
print(studentFromGroup("groupC"))
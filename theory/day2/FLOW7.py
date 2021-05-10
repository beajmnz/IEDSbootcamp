#! /usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 10 19:17:22 2021

@author: Bea Jimenez <bea.jimenez@alumni.ie.edu>
"""

"""
Our company has shops in the top 4 french cities. Select the city for which you
want to extract data.
"""


cities = ["paris","marseille","lyon","toulouse"]

city = ""

while city not in cities:
    city = input("Which city do you want to extract data for?\n").lower().strip()
    

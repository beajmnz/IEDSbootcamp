#! /usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 11 09:20:22 2021

@author: Bea Jimenez <bea.jimenez@alumni.ie.edu>
"""

"""
Write a Python program to sort (ascending and descending) a dictionary by value.
Tip: check the sorted function
"""

import operator

released = {"iphone" : 2007, "iphone 3G" : 2008, "iphone 3GS" : 2009, 
"iphone 4" : 2010, "iphone 4S" : 2011, "iphone 5" : 2012,
"iphone 5S" : 2013, "iphone 6" : 2014, "iphone 6S" : 2015, 
"iphone 7" : 2016, "iphone 8" : 2017, "iphone X" : 2017}

sortedDictAsc = sorted(released.items(), key = operator.itemgetter(0))

sortedDictDesc = sorted(released.items(), key = operator.itemgetter(0),reverse = True)

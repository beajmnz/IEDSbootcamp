#! /usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 11 09:46:03 2021

@author: Bea Jimenez <bea.jimenez@alumni.ie.edu>
"""

"""
Write a Python program to combine two dictionary adding values for
common keys.
d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
Sample output: Counter({'a': 400, 'b': 400, 'd': 400, 'c': 300})
Tip: check the Counter function from the collections module
"""

from collections import Counter

d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}

addedDict = dict(Counter(d1) + Counter(d2))

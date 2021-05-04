#! /usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  4 17:37:20 2021

@author: Bea Jimenez <bea.jimenez@alumni.ie.edu>
"""

"""
# Check if some of these 3 clients live in "Recoletos Street".
address1 = " RECOLETOS Street "
address2 = "recoletos st"
address3 = "Cibeles Square "
Extra exercise: can you create a variable named "total" with the total number of
times that "Recoletos street" appears?
"""

address1 = " RECOLETOS Street "
address2 = "recoletos st"
address3 = "Cibeles Square "

totalAddress = address1 + address2 + address3
total = totalAddress.lower().replace('street','st').count('recoletos st')
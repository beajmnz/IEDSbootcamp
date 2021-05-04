#! /usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  4 16:04:53 2021

@author: Bea Jimenez <bea.jimenez@alumni.ie.edu>
"""

borrowedMoney = float(input("enter the amount borrowed: "))

interestRatio = 4 / 100  # 4% annual interest
elapsedTime = 8 / 12 # 8 months
moneyPaidAfter8m = borrowedMoney * interestRatio * elapsedTime

print("\-nThe amount of money paid after 8 months is", moneyPaidAfter8m)
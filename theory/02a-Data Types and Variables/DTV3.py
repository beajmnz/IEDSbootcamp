#! /usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  4 16:16:59 2021

@author: Bea Jimenez <bea.jimenez@alumni.ie.edu>
"""

"""
You have a debt of 50k€. You compare different deposits and the most
profitable one is a deposit in Santander with a 6% annual compound interest.
How much money should you invest in that deposit to have 50k€ in N years?

FV = P* (1+I)**N
"""

FV = 50000 # 50k€
I = 6/100 # 6%
N = float(input("Input the number of years you want to return the money in: "))


P = 50000 / (1+I)**N

print("\nyou would need to invest","{:.2f}".format(P),"right now in order to make",FV,"in",N,"years")



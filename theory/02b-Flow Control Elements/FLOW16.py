#! /usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 10 20:19:36 2021

@author: Bea Jimenez <bea.jimenez@alumni.ie.edu>
"""

"""
You are working in a Russian travel agency and while organizing the
trip, your users would like to convert some money.
Write a python program that is able to convert EUR/RUB or RUB/EUR
currencies.
Ask the user what kind of exchange he is looking for and print the
received amount.
Rates:
1 EUR = 79.48 RUB
"""

eur2rub = 79.48
exchange = ""

while exchange not in ["EUR/RUB","RUB/EUR"]:
    exchange = input("Please select EUR/RUB or RUB/EUR\n")
    
amount = float(input("Please enter the amount to exchange\n"))

if exchange == "EUR/RUB":
    print("You will get","{:.2f}".format(amount*eur2rub),"RUB")
else:
    print("You will get","{:.2f}".format(amount/eur2rub),"EUR")

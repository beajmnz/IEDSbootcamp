#! /usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 18 16:45:28 2021

@author: Bea Jimenez <bea.jimenez@alumni.ie.edu>
"""

"""
Money notes
===========

In the EU, there are bank notes of 5, 10, 20, 50, 100, 200, and 500 EUR.

The user introduces two numbers:

the price to pay (for simplicity, a multiple of 5); and
one of the bank notes available.
The program must:

verify that the numbers given are meaningful (e.g. that the bank note given is larger than the price to pay)
calculate how much money must be returned; and
determine the best way to return that money given the available bank notes.
"""


price2pay = int(input("Enter the price to pay (multiple of 5)\n"))

given_bank_note = int(input("Enter the bank note you give to pay\n"))

available_bank_notes = [500, 200, 100, 50, 20, 5]
dict_money2return = dict()
if given_bank_note in available_bank_notes:
    money2return = given_bank_note - price2pay
    for bank_note in available_bank_notes:
        nr_bank_notes = money2return // bank_note
        if nr_bank_notes > 0:
            dict_money2return[bank_note] = nr_bank_notes
            money2return = money2return - nr_bank_notes * bank_note
    print(money2return)
    print(dict_money2return)
else:
    print("You gave a counterfeit bank note!")

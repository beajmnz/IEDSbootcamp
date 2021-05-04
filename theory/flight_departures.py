#! /usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  4 18:35:12 2021

@author: Bea Jimenez <bea.jimenez@alumni.ie.edu>
"""

# AIRPORT

f1 = "MAD-BCN"
f2 = "LON-MAD"
f3 = "MAD-SEV"
f4 = "MAD-SEV"
f5 = "PAR-LON"

# HM times was Madrid the departure

flights = f1+f2+f3+f4+f5

airport = input('what airport are you looking flights from? ')

departures = flights.count(airport+'-')

print('there are',departures,'flighs departing from',airport)
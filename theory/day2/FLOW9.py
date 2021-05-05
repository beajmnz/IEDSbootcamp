#! /usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  5 15:54:05 2021

@author: Bea Jimenez <bea.jimenez@alumni.ie.edu>
"""

"""
Write a Python program to open 4 important European newspapers in
your browser using a for loop.

Tip: use the command open(url) from the webbrowser library
"""

import webbrowser

newspapers = ['http://www.elpais.es','https://www.faz.net','https://www.lefigaro.fr/','https://www.lastampa.it/']

for n in newspapers:
    webbrowser.open(n)
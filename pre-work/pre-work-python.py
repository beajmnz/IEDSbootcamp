#! /usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 23 17:39:23 2021

@author: Bea Jimenez <bea.jimenez@alumni.ie.edu>
"""

#Complete the following exercises using Spyder or Google Collab (your choice):
#1. Print your name

print('Bea Jimenez')


#2. Print your name, your nationality and your job in 3 different lines with one single 
#print command

print('Bea Jimenez\nSpanish\nCurrently unemployed, but I\'m a COO wannabe :)')

#3. Create an integer variable taking the value 4

intFour = 4

#4. Create other integer variable taking the value 1

intOne = 1

#5. Transform both variables into boolean variables. What happens?

intFour = bool(intFour)
intOne = bool(intOne)

#  -> both variables are transformed into booleans and get True value

#6. Transform this variable "23" into numerical variable.
str23 = '23'
int23 = int(str23)


#7. Ask the user their age in the format 1st Jan, 2019 (check the command input for 
#this). Using this info, show on the screen their year of birth

birthdate = input(prompt='Please state your birthdate in the format 1st Jan, 2019')
print('From what you just told me, you were born in the year '+birthdate[-4:])

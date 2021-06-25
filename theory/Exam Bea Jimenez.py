#! /usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 31 12:35:32 2021

@author: Bea Jimenez <bea.jimenez@alumni.ie.edu>
"""

"""
Have a look to the restaurants data in the Excel file named "Exam restaurants data".
Each row shows one restaurant for an international brand.
The following info is given in every row:
- restaurantid: unique ID to identify the restaurant
- iyear, imonth and iday: year, month & day when the rest. opened
- country_txt and region_txt: country and world region where the rest was opened
- restauranttype_txt: kind of restaurant
- employees: number of employees in the restaurant
"""


import pandas as pd
from datetime import datetime

datos = pd.read_excel("Exam restaurants data.xlsx", sheet_name="Restaurants")

"""
E1. Which are the 10 restaurants with the most employees?
"""

# in order to get the 10 restaurants with the most employees we sort
# our dataframe based on the employees column and show the top 10 values
datos.sort_values(by="employees", ascending=False).head(10)


"""
E2. Which are the 4 regions with the highest total number of employees?
"""

# in order to get the 4 regiones with the hightst total number of employees
# we first group by region selecting the employees column and adding their values
# and then we order by values in descending order and get the top 4 regions
datos.groupby(by="region_txt").employees.sum().sort_values(ascending=False).head(4)


"""
E3. Find the biggest restaurant per country in terms of number of employees
"""

# we first sort our dataframe by the number of employees in descending order, then
# remove the rows where the country_txt and keep the first occurrence (defailt value)
# and show restaurantId, country and employees so that we can better see the result
datos.sort_values(by="employees", ascending=False).drop_duplicates(
    subset="country_txt"
).loc[:, ["restaurantid", "country_txt", "employees"]]


"""
E4. How many restaurants do we have per Region and Type?
"""

# in order to show the amount of restaurants per region and type we create a crosstab
# with those two colums
pd.crosstab(datos.region_txt, datos.restauranttype_txt)

"""
E5. Obtain a dataframe where every row is one country, every column a type and the
total number of exployees is given in the values inside this dataframe
"""

# we can get the desired dataframe by grouping by country and type, adding the
# number of employees and then unstacking
datos.groupby(by=["country_txt", "restauranttype_txt"]).employees.sum().unstack()


"""
E6. How many restaurants in India have more than 30 employees
"""

# if we filter our dataframe by country equal to India and number of employees
# greater than 30 we obtain a reduced dataframe. checking its length or the first
# value in the shape tuple gives us the number we are looking for
datos.loc[(datos.country_txt == "India") & (datos.employees > 30)].shape[0]


"""
E7. How many big restaurants do we have per region? Big means more than 40 
employees
"""

# first we filter for bit restaurants and then we count values by region so
# that we can get the total number
datos.loc[datos.employees > 40].region_txt.value_counts()


"""
E8. Create a script to extract the hours from a string with the following format:
    Expected input:            Expected output
     "March 17, 11:28:00"             11
     "May 5, 9:12:50"                  9

    
"""


def extract_hours(date_string):
    """Extracts the hours indicated in a date string with the format
    \" March 17, 11:28:00\" -> 11"""
    date_dt = datetime.strptime(date_string, "%B %d, %H:%M:%S")
    return date_dt.hour


extract_hours("May 5, 9:12:50")


"""
E9. Create a script to show the body mass index to the user. The user will give his
weight in kilos and his height in cms and the body mass index will be printed
according to the following formula:
body mass index = weight in kilos / (height in m) 2
"""


def body_mass_index():
    """Calculates the BMI based on user input"""
    weight = float(input("Please input your weight in kilos\n"))
    height = float(input("Please input your height in cms\n"))
    print("Your BMI is", "{:.2f}".format(weight / ((height / 100) ** 2)))


body_mass_index()

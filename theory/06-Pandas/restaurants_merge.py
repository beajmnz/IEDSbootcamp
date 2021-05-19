#! /usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 17 19:08:17 2021

@author: Bea Jimenez <bea.jimenez@alumni.ie.edu>
"""

import pandas as pd

# read excel sheets
restaurants = pd.read_excel("Restaurants merge.xlsx", sheet_name="Restaurants")
bookings = pd.read_excel("Restaurants merge.xlsx", sheet_name="Bookings")
events = pd.read_excel("Restaurants merge.xlsx", sheet_name="Events")
directors = pd.read_excel("Restaurants merge.xlsx", sheet_name="Directors")
employees = pd.read_excel("Restaurants merge.xlsx", sheet_name="Employees")


"""Global KPIs"""

# 0.1. How many restaurants do we have?

print("We have", restaurants.shape[0], "restaurants")

# 0.2. How many workers are in total? How many clients were attended?

print("There are", employees.shape[0], "employees")
print("There were", bookings.clients.sum(), "clients in the restaurants")


# 0.3. How much income was generated in bookings? And in events?
# How much money is spent in Salaries?

print(
    "The income generated was",
    "${:,.2f}".format(bookings.total_bill.sum()),
    "from bookings and",
    "${:,.2f}".format(events.Price.sum()),
    "from events.",
)


"""Pandas Review"""
# 1.1 Show the total capacity by country

restaurants.loc[:, ["Country", "Capacity"]].groupby(
    by=["Country"], as_index=False
).sum().sort_values(by="Capacity", ascending=0)

# 1.2. Which is the percentage of restaurants by type in every country?
# 1.3. How many different nationalities are there in the employees table?

employees.loc[:, ["Nationality"]].drop_duplicates().shape[0]

# 1.4. Which is the average salary for the directors over 35. How many directors are?

print(
    "There are",
    directors.loc[directors.Age > 35, :].shape[0],
    "directors over 35, with an average salary of",
    "{:,.2f}".format(directors.loc[directors.Age > 35, :].Salary.mean()),
)

# 1.5. Which male and female director has the highest salary?

directors.sort_values(by=["Gender", "Salary"], ascending=[0, 0])

# 1.6. How many bookings are there by day? And by day and time?

bookings.groupby(by=["day"], as_index=False).size()

bookings.groupby(by=["day", "time"], as_index=False).size()

# 1.7. How much was the total bill for the Café restaurants? And how many
# bookings did we have for these café restaurants? (Do not use merge)

cafe_rest = tuple(restaurants.loc[restaurants.Type == "Cafe", ["Code"]].Code)
bookings.loc[bookings.restaurant.isin(cafe_rest), :]

print(
    "There where",
    bookings.loc[bookings.restaurant.isin(cafe_rest), :].shape[0],
    "bookings in cafe restaurants for a total of",
    "{:,.2f}".format(
        bookings.loc[bookings.restaurant.isin(cafe_rest), :].total_bill.sum()
    ),
)

# 1.8. Add a category column in "Directors" based on the Salary: A (>45k), C (<20k), B (other cases)

"""Plotnine review
2.1. Are correlated the variables Age and Salary for the directors? Repeat the graph showing the director's gender as well.
2.2. Build a graph with the 3 directors with the highest salaries.
2.3. Build a graph to show the most profitable weekday in terms of total income in bills
2.4. Build a graph to show the bills distribution by city. Repeat the previous exercise using facet_grid
2.5. Create a graph to show the number of events by type"""

"""Merge commands"""
# 3.1. Add a column named "Number Of Directors" in Restaurants. How many directors are there by country?

# first we get the number of directors for each restaurant
dir_per_rest = directors.groupby(by="Restaurant", as_index=False).size()
dir_per_rest.columns = ["Code", "# of directors"]
# then we merge the two tables
rest_directors = pd.merge(left=restaurants, right=dir_per_rest, on="Code", how="left")

rest_directors.loc[:, ["Country", "# of directors"]].groupby(
    by="Country", as_index=False
).sum().sort_values(by="# of directors", ascending=0)

# 3.2. Show the salary and the generated money in events by director

event_per_dir = (
    events.loc[:, ["Director", "Price"]].groupby(by="Director", as_index=False).sum()
)

pd.merge(
    left=directors, right=event_per_dir, left_on="Id", right_on="Director", how="left"
).loc[:, ["Id", "Name", "Surname", "Salary", "Price"]].sort_values(
    by="Price", ascending=0
)

# 3.3. Show the total cumulated bill by employees' gender

bill_per_waiter = bookings.groupby(by="waiter", as_index=False).total_bill.sum()
empl_and_bill = pd.merge(
    left=employees,
    right=bill_per_waiter,
    how="left",
    left_on="WaiterId",
    right_on="waiter",
)
empl_and_bill.loc[:, ["Gender", "total_bill"]].groupby(
    by="Gender", as_index=False
).sum()


# 3.4. Who was the best waiter (regarding to the total generated income) by nationality?

empl_and_bill.sort_values(by="total_bill", ascending=0).drop_duplicates(
    subset="Nationality"
)


# 3.5. Calculate the capacity and total clients attended by restaurant. Show the proportion and show the top 3 restaurants
# 3.6. How much money earned in tips the oldest waiter? How many breakfasts, lunches and dinners did he work?
# 3.7. How many events by type were sold by female directors? Which was the total price for these events?
# 3.8. Show how many A, B and C directors we have by restaurant location (country) [Note: A,B,C were calculated in exercise 1.8)
# 3.9. Calculate the average price of the events by event type and restaurant type
# 3.10. Build a table to show by restaurant these variables: clients attended in bookings, clients attended in events,number of events and total capacity of the restaurant

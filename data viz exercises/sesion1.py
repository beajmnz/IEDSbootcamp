#! /usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  7 12:38:14 2021

@author: Bea Jimenez <bea.jimenez@alumni.ie.edu>
"""

import pandas as pd
from plotnine import *

data = pd.read_excel("Bar.xlsx")
data = data.reindex(columns=bar.columns[:-4])

# 1.- Are the variables “bills” and “tips” correlated?

ggplot(aes(x="bill", y="tip"), data) + geom_point()

data.bill.corr(data.tip)


# Repeat the graph showing the “gender”.

ggplot(aes(x="bill", y="tip", color="gender"), data) + geom_point()


# 2.- Are the variables “bills” and “orders” correlated?.

ggplot(aes(x="bill", y="orders"), data) + geom_point()

data.bill.corr(data.orders)


# 3.- Create a plot and show how many days each “gender” works.

ggplot(aes(x="gender"), data) + geom_bar()


# 4.- Create a plot to show how many days we had by type of “service”.

ggplot(aes(x="service"), data) + geom_bar()


# 4.- 4b. Create the previous plot horizontally. Only with the
# type of “service”: “very good”, “excellent” and “brilliant”.

data_good_service = data[data.service.isin(["very good", "excellent", "brilliant"])]
ggplot(aes(x="service", fill="service"), data_good_service) + geom_bar() + coord_flip()


# 5.- Create a graph to show how much money each
# “gender” made in “bills” in the “year” 2019.

data_2019 = (
    data[data.year.eq(2019)]
    .loc[:, ["bill", "gender"]]
    .groupby(by="gender", as_index=False)
    .sum()
)

ggplot(aes(x="gender", y="bill"), data_2019) + geom_bar(stat="identity")

# OPTION2

data_2019 = data[data.year.eq(2019)].loc[:, ["bill", "gender"]]

ggplot(aes(x="gender", y="bill", fill="gender"), data_2019) + geom_bar(stat="sum")


# 6.- Create a graph showing the “week_day” plus the
# number of “orders” for each type of “service”.

data_week_day = (
    data.loc[:, ["week_day", "orders", "service"]]
    .groupby(by=["service", "week_day"], as_index=False)
    .sum()
)
ggplot(aes(x="factor(week_day)", y="orders", fill="service"), data_week_day) + geom_bar(
    stat="identity", position="dodge"
)


# 7.- Create a plot to show the total “orders per week_day"

data_week_day = (
    data.loc[:, ["week_day", "orders"]].groupby(by=["week_day"], as_index=False).sum()
)
ggplot(aes(x="week_day", y="orders"), data_week_day) + geom_line()


# 7b.- Following the previous plot show the total “orders” per “week_day ”
# and “gender"

data_week_day_gender = (
    data.loc[:, ["week_day", "orders", "gender"]]
    .groupby(by=["week_day", "gender"], as_index=False)
    .sum()
)
ggplot(aes(x="week_day", y="orders", color="gender"), data_week_day_gender) + geom_line(
    size=5
)


# 8.- Create a plot to show the total “orders” per “month” by 4 “nationalities”.
# (choose the nationalities you prefer).
data_mon_nat = (
    data.loc[
        data.nationality.isin(["Spanish", "German", "French", "Italian"]),
        ["month", "orders", "nationality"],
    ]
    .groupby(by=["month", "nationality"], as_index=False)
    .sum()
)
ggplot(aes(x="month", y="orders", color="nationality"), data_mon_nat) + geom_line(
    size=5
)


# 8b.- Following the previous plot, add the different “years”.
data_mon_nat_year = (
    data.loc[
        data.nationality.isin(["Spanish", "German", "French", "Italian"]),
        ["month", "orders", "nationality", "year"],
    ]
    .groupby(by=["month", "nationality", "year"], as_index=False)
    .sum()
)
(
    ggplot(aes(x="month", y="orders", color="nationality"), data_mon_nat_year)
    + geom_line(size=3)
    + facet_grid(("year", "."))
)


# 9. Create an histogram where we can observe how are the “bills” distributed.
ggplot(aes(x="bill"), data) + geom_histogram()
# to remove the outlier
ggplot(aes(x="bill"), data) + geom_histogram() + xlim(0, 2000)


# 9b. Following the previous plot, create several histograms per
# type of “service”.

(
    ggplot(aes(x="bill", fill="service"), data)
    + geom_histogram()
    + facet_grid(("service", "."))
)

ggplot(aes(x="bill", fill="service"), data) + geom_histogram()


# 10.- Analyze the “bill” distribution per “service” and “year”.
(
    ggplot(aes(x="bill", fill="service"), data)
    + geom_density()
    + facet_grid(("year", "service"))
)


# 11.- Create a boxplot where we can see the distribution between
# “genders”, type of “service” and “tips”.

ggplot(aes(x="gender", y="tip", fill="service"), data) + geom_boxplot()


# 12. Create the same graph showing the different “years” too.

(
    ggplot(aes(x="gender", y="tip", fill="service"), data)
    + geom_boxplot()
    + facet_wrap("year")
)


# 13. Create a heatmap showing the total “orders” per “month”
# and “day” of the year 2020.

data_2020 = data[data.year.eq(2020)].loc[:, ["orders", "month", "day"]]

ggplot(aes(x="day", y="month", fill="orders"), data_2020) + geom_tile()


# 15. Create a barplot to show the total number of “orders” by type of “service”.

ggplot(aes(x="service", y="orders", fill="service"), data) + geom_bar(stat="identity")


# 16. How many “days” were there by type of “service”?

ggplot(aes(x="service", fill="service"), data) + geom_bar()


# 18. Build a graph with the 3 “nationalities” with the least amount in “tips”.

data_least_tips = (
    data.loc[:, ["tip", "nationality"]]
    .groupby(by="nationality", as_index=False)
    .sum()
    .sort_values(by="tip", ascending=False)
    .tail(3)
)
ggplot(aes(x="nationality", y="tip", fill="nationality"), data_least_tips) + geom_bar(
    stat="identity"
)


# 19. Create a graph to show average sold “items” by “gender” and “nationality”.

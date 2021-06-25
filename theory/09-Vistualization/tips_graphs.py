#! /usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  1 17:27:27 2021

@author: Bea Jimenez <bea.jimenez@alumni.ie.edu>
"""

import seaborn as sns
from plotnine import *

tips = sns.load_dataset("tips")
tips.head()

# 1.- show the total bill per day

plot_info = tips.loc[:, ["total_bill", "day"]].groupby(by="day", as_index=False).sum()

ggplot(aes(x="day", y="total_bill"), plot_info) + geom_bar(stat="identity")

# 2.- show the average bill per day and time (do not use a barplot)

plot_info = (
    tips.loc[:, ["total_bill", "day", "time"]]
    .groupby(by=["day", "time"], as_index=False)
    .mean()
)

(
    ggplot(aes(x="day", y="time", fill="total_bill"), plot_info)
    + geom_tile()
    + scale_fill_gradient(low="red", high="green")
)


# 3.- Are the total bills equally distributed per day?
# Do we have significant differences per day?

ggplot(aes(x="day", y="total_bill"), tips) + geom_boxplot()


# 4.- Build a barplot with the % of bookings per day and time


# 5.- Show in a heatmap the percentage of bookings per day and time
plot_info = pd.crosstab(tips.day, tips.time, normalize="all")
plot_info = plot_info.melt()

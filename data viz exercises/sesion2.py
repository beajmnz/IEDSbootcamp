#! /usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 10 12:36:56 2021

@author: Bea Jimenez <bea.jimenez@alumni.ie.edu>
"""
import pandas as pd
from plotnine import *

bar = pd.read_excel("Bar.xlsx")
bar = bar.reindex(columns=bar.columns[:-4])

# 14. Create a heatmap showing the different types of “services”
# by “supervisor” (don't use groupby command).

bar2 = pd.crosstab(bar.supervisor, bar.service)
bar2.reset_index(inplace=True)
bar2 = pd.melt(bar2, id_vars=["supervisor"])

(
    ggplot(aes(x="service", y="supervisor", fill="value"), bar2)
    + geom_tile()
    + geom_text(aes(label="value"), size=9)
)

# 14b. When you finish put in order the “services”.

bar2["service"] = pd.Categorical(
    bar2.service, categories=["brilliant", "excellent", "very good", "good", "normal"]
)

(
    ggplot(aes(x="service", y="supervisor", fill="value"), bar2)
    + geom_tile()
    + geom_text(aes(label="value"), size=9)
)


# 17. Using a graph, show which “nationality” has the highest number of
# “items” sold.  Try to show the bars sorted from the top to the lowest.

bar3 = (
    bar.groupby(by=["nationality"], as_index=False)
    .sum()
    .sort_values(by="items", ascending=False)
)
bar3["nationality"] = pd.Categorical(bar3.nationality, categories=bar3.nationality)

(
    ggplot(aes(x="nationality", y="items", fill="nationality"), bar3)
    + geom_bar(stat="identity")
    + geom_text(
        aes(label="items"), position=position_stack(vjust=1.05), size=10, color="black"
    )
)

# 21. Build a proper graph to show the Correlation Matrix.

bar4 = bar.corr()
bar4.reset_index(inplace=True)
bar4 = pd.melt(bar4, id_vars=["index"])

bar4.columns = ["variable1", "variable2", "correlation"]
bar4.correlation = bar4.correlation.round(2)

(
    ggplot(aes(x="variable1", y="variable2", fill="correlation"), bar4)
    + geom_tile()
    + scale_fill_gradient2(limits=[-1, 1])
    + geom_text(aes(label="correlation"), size=9)
)

# 22. Create a graph showing only the highest bill per nationality
# considering only bills between 500 and 1000 euros.

bar5 = bar.loc[bar.bill.between(500, 1000), ["nationality", "bill"]]
bar5 = bar5.sort_values(by="bill", ascending=False)
bar5 = bar5.drop_duplicates("nationality", keep="first")
bar5["bill"] = bar5.bill.round(2)

(
    ggplot(aes(x="nationality", y="bill", fill="nationality"), bar5)
    + geom_bar(stat="identity")
    + geom_text(
        aes(label="bill"), position=position_stack(vjust=1.05), size=6, color="black"
    )
    + scale_fill_brewer(type="seq", pallete="Blue")
)

# 23. Create a lineplot to show the total orders per month for the
# top 4 nationalities.


# 25. Create a graph showing the average for the 10 highest
# bills per nationality.

bar6 = bar.loc[:, ["nationality", "bill"]]
bar6 = bar6.sort_values(by="bill", ascending=False)
bar6 = bar6.groupby(by="nationality", as_index=False).head(10)

bar6 = bar6.groupby(by="nationality", as_index=False).mean()
bar6.bill = bar6.bill.round().astype(int)

(
    ggplot(aes(x="nationality", y="bill", fill="nationality"), bar6)
    + geom_bar(stat="identity")
    + geom_text(
        aes(label="bill"), position=position_stack(vjust=1.05), size=6, color="white"
    )
    + theme(panel_background=(element_rect(fill="black")))
    + ggtitle("average of the 10 highest bills by nationality")
    + xlab("countries")
    + ylab("average")
)

# 26. Proportions of brilliant, good...... days per supervisor.

bar7 = bar.loc[:, ["service", "supervisor", "gender"]]
bar7 = bar7.groupby(by=["supervisor", "service"], as_index=False).count()

(
    ggplot(aes(x="supervisor", y="gender", fill="service"), bar7)
    + geom_bar(stat="identity", position="fill")
    + theme(
        axis_text=element_text(angle=90), panel_background=(element_rect(fill="white"))
    )
    + geom_text(
        aes(y="gender", label="gender"),
        position=position_fill(vjust=1.05),
        size=6,
        color="black",
    )
)


# 28. Create a graph showing the max, min and mid of the orders per kind of service and gender.

bar8 = bar.loc[:, ["service", "orders", "gender"]]
bar8 = (
    bar8.groupby(by=["gender", "service"])
    .agg(maximum=("orders", "max"), minimum=("orders", "min"), mid=("orders", "mean"))
    .reset_index()
)
bar8 = pd.melt(bar8, id_vars=["gender", "service"])
bar8["service"] = pd.Categorical(
    bar8.service, categories=["brilliant", "excellent", "very good", "good", "normal"]
)

(
    ggplot(aes(x="service", y="value", fill="variable"), bar8)
    + geom_bar(stat="identity", position="stack")
    + facet_grid(("gender", "."))
)


# 29. Create a line plot showing the total orders per 4 nationalities and year
#  and add the full name of the months in the Xlab

months = {
    1: "Jan",
    2: "Feb",
    3: "Mar",
    4: "Apr",
    5: "May",
    6: "Jun",
    7: "Jul",
    8: "Aug",
    9: "Sep",
    10: "Oct",
    11: "Nov",
    12: "Dec",
}

natl = ("Spanish", "Mexican", "French", "German")

bar9 = bar.loc[bar.nationality.isin(natl), ["orders", "nationality", "year", "month"]]
bar9.month = bar9.month.map(months)
bar9["month"] = pd.Categorical(
    bar9.month,
    categories=[
        "Jan",
        "Feb",
        "Mar",
        "Apr",
        "May",
        "Jun",
        "Jul",
        "Aug",
        "Sep",
        "Oct",
        "Nov",
        "Dec",
    ],
)

bar9 = bar9.groupby(by=["year", "month", "nationality"], as_index=False).sum()

(
    ggplot(aes(group="nationality", x="month", y="orders", color="nationality"), bar9)
    + geom_line()
    + facet_grid(("year", "."))
    + theme(axis_text=element_text(angle=45))
)

# 30. Create a heatmap showing the total tips per day and month of the year 2020.
# 30b. Same graph but only taking the first 6 months and the first 15 days and
# add the numbers in each tile.

bar10 = bar.loc[
    bar.year.eq(2020) & bar.day.isin(range(16)) & bar.month.isin(range(7)),
    ["tip", "month", "day"],
]
bar10.tip = bar10.tip.round(2)
bar10.month = bar10.month.map(months)
bar10["month"] = pd.Categorical(
    bar10.month,
    categories=[
        "Jan",
        "Feb",
        "Mar",
        "Apr",
        "May",
        "Jun",
    ],
)
bar10 = bar10.groupby(by=["month", "day"], as_index=False).sum()

(
    ggplot(aes(x="factor(day)", y="factor(month)", fill="tip"), bar10)
    + geom_tile(aes(width=0.95, height=0.95))
    + geom_text(aes(label="tip"), size=5)
    + xlab("day")
    + ylab("month")
    + scale_fill_gradient(low="#D3D3D3", high="Blue")
)

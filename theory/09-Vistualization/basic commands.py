#! /usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 31 15:40:45 2021

@author: Bea Jimenez <bea.jimenez@alumni.ie.edu>
"""

from plotnine import *

from plotnine.data import diamonds

diamonds.head(3)

ggplot(aes(x="carat", y="price"), diamonds) + geom_point()


import seaborn as sns

tips = sns.load_dataset("tips")
tips.head()


# 1. build a scatterplot for the total bills and the tips,
ggplot(aes(x="total_bill", y="tip"), tips) + geom_point()

# 2. repeat the same grapth but show also the sex of the waiter
(
    ggplot(aes(x="total_bill", y="tip", color="sex"), tips)
    + geom_point()
    + ggtitle("Tips vs Total bill")
    + xlab("Invoice")
)


ggplot(aes(x="price"), diamonds) + geom_histogram()

ggplot(aes(x="price", fill="cut"), diamonds) + geom_histogram()


for diamond_type in diamonds.cut.unique():
    print(
        ggplot(aes(x="price"), diamonds.loc[diamonds.cut == diamond_type])
        + geom_histogram()
        + ggtitle("Histogram for {} diamods".format(diamond_type))
    )


ggplot(aes(x="price"), diamonds) + geom_histogram() + facet_wrap(("cut"))

ggplot(aes(x="price"), diamonds) + geom_histogram() + facet_grid(("clarity", "cut"))


ggplot(aes(x="clarity"), diamonds) + geom_bar()

ggplot(aes(x="clarity", fill="cut"), diamonds) + geom_bar() + facet_wrap(("cut"))

"""
1. number of bookings per day

2. number of bookings per day and time

3. number of bookings per day, time and smoker area

4. number of bookings per day, time, smoker area and sex
"""

ggplot(aes(x="day"), tips) + geom_bar()

ggplot(aes(x="day", fill="time"), tips) + geom_bar()

ggplot(aes(x="day", fill="time"), tips) + geom_bar() + facet_wrap(("smoker"))

ggplot(aes(x="day", fill="time"), tips) + geom_bar() + facet_grid(("smoker", "sex"))

ggplot(aes(x="day"), tips) + geom_bar() + coord_flip()


desired_colors = ["I", "G", "H"]

(
    ggplot(aes(x="color"), diamonds.loc[diamonds.color.isin(desired_colors), :])
    + geom_bar()
)


# ggplot(aes(x="price"), diamonds) + geom_density()
# makes the computer crash


# plot in a density graph how the total bills are distributed per day

# ggplot(aes(x="total_bill"), tips) + geom_density() + facet_wrap(("day"))

(
    ggplot(aes(x="cut", y="price", fill="clarity"), diamonds)
    + geom_boxplot()
    + facet_wrap(("clarity"))
)

(
    ggplot(aes(x="cut", y="price", fill="clarity"), diamonds)
    + geom_boxplot()
    + facet_wrap(("clarity"))
    + coord_flip()
)


(
    ggplot(aes(x="carat", y="price", color="price"), diamonds)
    + geom_point()
    + scale_color_gradient(low="red", high="green")
)

# scale_color_gradient for continous variables
(
    ggplot(aes(x="carat", y="price", color="price"), diamonds)
    + geom_point()
    + scale_color_gradient(low="red", high="green")
)

# scale_color_brewer for discrete variables
# check www.colorbrewer2.org for the brewer options
(
    ggplot(aes(x="carat", y="price", color="clarity"), diamonds)
    + geom_point()
    + scale_color_brewer(type="qualitative", palette="Pastel1")
)

# scale_fill_gradient y scale_fill_brewer funcionan igual pero modificando el relleno


p = ggplot(aes(x="price"), diamonds) + geom_histogram()
p + theme(
    axis_text=element_text(size=20, color="green"),
    axis_text_x=element_text(color="red"),
)

p + theme_xkcd()

#! /usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  1 15:58:32 2021

@author: Bea Jimenez <bea.jimenez@alumni.ie.edu>
"""

import pandas as pd
from plotnine import *

url = "https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv"
chipo = pd.read_csv(url, sep="\t")

plot_info = (
    chipo.loc[:, ["item_name", "quantity"]]
    .groupby(by="item_name", as_index=False)
    .sum()
    .sort_values(by="quantity", ascending=False)
    .head(10)
)

chipo_plot = (
    ggplot(aes(x="item_name", y="quantity"), plot_info)
    + geom_bar(stat="identity")
    + coord_flip()
    + theme_xkcd()
)

chipo_plot.save("Chipo_plot.jpg")

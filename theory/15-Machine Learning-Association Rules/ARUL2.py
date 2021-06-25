#! /usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 24 16:46:49 2021

@author: Bea Jimenez <bea.jimenez@alumni.ie.edu>
"""

import pandas as pd
from datetime import datetime
from mlxtend.frequent_patterns import apriori, association_rules
from mlxtend.preprocessing import TransactionEncoder
from plotnine import *


data = pd.read_csv("Online Retail_Association rules_v2.csv", encoding="Latin-1")

data["income"] = data.Quantity * data.UnitPrice

products = data.groupby(by=["StockCode", "Description"]).sum()
products.sort_values(by="income", ascending=False).head(3)

data.head()


# Give a calendar heatmap for the number of sold items per day in United Kingdom
# during December 2010 and January 2011

data.InvoiceDate = pd.to_datetime(data.InvoiceDate)
dataUK = data.loc[
    (data.Country == "United Kingdom")
    & (data.InvoiceDate >= "2010-12-01")
    & (data.InvoiceDate < "2011-01-31"),
    :,
]

dataUKDate = dataUK.groupby(by="InvoiceDate", as_index=False).count()
dataUKDate["day"] = dataUK.InvoiceDate.dt.day
dataUKDate["month"] = dataUK.InvoiceDate.dt.month

ggplot(aes(x="day", y="month", fill="Quantity"), dataUKDate) + geom_tile()

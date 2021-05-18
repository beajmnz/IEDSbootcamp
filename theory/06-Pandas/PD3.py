#! /usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 17 15:26:05 2021

@author: Bea Jimenez <bea.jimenez@alumni.ie.edu>
"""

"""
With the chipo data: 
1. How many items are more expensive than 10$?
2. What is the price of each item when only 1 item is bought?
3. Sort by the name of the item
4. What was the quantity of the most expensive item ordered?
5. How many times were a Veggie Salad Bowl ordered?
6. How many times people ordered more than one Canned Soda?
7. How many units where sold by item_name?
"""

import pandas as pd

url = "https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv"
chipo = pd.read_csv(url, sep="\t")

# 1. How many items are more expensive than 10$?

chipo["item_price_num"] = chipo.item_price.apply(lambda x: float(x[1:]))

chipo.loc[chipo.item_price_num > 10, :].shape[0]


# 2. What is the price of each item when only 1 item is bought?

chipo.loc[chipo.quantity == 1, :].loc[
    :, ["item_name", "item_price_num"]
].drop_duplicates(subset="item_name", keep="first")

# extra

chipo.loc[chipo.quantity == 1, :].loc[
    :, ["item_name", "item_price_num"]
].drop_duplicates(subset="item_name", keep="first").sort_values(
    by="item_price_num", ascending=0
)


# 3. Sort by the name of the item

chipo.loc[chipo.quantity == 1, :].loc[
    :, ["item_name", "item_price_num"]
].drop_duplicates(subset="item_name", keep="first").sort_values(
    by="item_name", ascending=1
)


# 4. What was the quantity of the most expensive item ordered?

chipo.loc[
    chipo.item_name
    == chipo.loc[chipo.quantity == 1, :]
    .loc[:, ["item_name", "item_price_num"]]
    .drop_duplicates(subset="item_name", keep="first")
    .sort_values(by="item_price_num", ascending=0)
    .item_name[0],
    :,
].quantity.max()


# 5. How many times were a Veggie Salad Bowl ordered?

chipo.loc[chipo.item_name == "Veggie Salad Bowl", :].shape[0]

# 6. How many times people ordered more than one Canned Soda?


chipo.loc[((chipo.item_name == "Canned Soda") & (chipo.quantity > 1)), :].shape[0]


# 7. How many units where sold by item_name?

chipo.loc[:, ["item_name", "quantity"]].groupby(by="item_name", as_index=False).sum()

# 8. Top 3 more profitable item names (greater added price)

chipo.loc[:, ["item_name", "item_price_num"]].groupby(
    by="item_name", as_index=False
).sum().sort_values(by="item_price_num", ascending=False).head(3)

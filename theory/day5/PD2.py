#! /usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 10 16:56:09 2021

@author: Bea Jimenez <bea.jimenez@alumni.ie.edu>
"""

"""
Write on your console:
url = 'https://raw.githubusercontent. justmarkham /DAT8/master/ chipotle.tsv
chipo = pd.read_csv url , sep = t')
For these data:
1. have a look to the first 10 entries. What are the data about?
2. How many observations do we have in the data?
3. What is the number of columns in the dataset? Print the name of all columns
4. How is the dataset indexed?
5. Which was the most ordered item in times?
6. How many items of this product were ordered?
7. What was the most ordered item in the choice_description column?
8. How much was the revenue for the period in the dataset?
9. How many items were ordered in total?
10. How many orders were made in the period?
11. What is the average amount per order? (not yet)
12. How many different items are sold?
"""

import pandas as pd

url = 'https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv'
chipo = pd.read_csv(url , sep = '\t')

# 1. have a look to the first 10 entries. What are the data about?
chipo.head(10)

# 2. How many observations do we have in the data?
chipo.shape[0]

# 3. What is the number of columns in the dataset? Print the name of all columns
chipo.shape[1]
chipo.columns

# 4. How is the dataset indexed?
chipo.index

# 5. Which was the most ordered item in times?
chipo.item_name.value_counts().idxmax()  # también vale  .index[0]

# 6. How many items of this product were ordered?
chipo.item_name.value_counts()[0]

# 7. What was the most ordered item in the choice_description column?
chipo.choice_description.value_counts().idxmax()

# 8. How much was the revenue for the period in the dataset?
chipo.item_price.str.replace('$','').astype(float).sum()
chipo.item_price.apply(lambda x:float(x[1:])).sum()

# 9. How many items were ordered in total?
chipo.quantity.sum()

# 10. How many orders were made in the period?
chipo.drop_duplicates(subset=["order_id"]).shape[0]


# 11. What is the average amount per order? (not yet)


# 12. How many different items are sold?
chipo.drop_duplicates(subset="item_name").shape[0]

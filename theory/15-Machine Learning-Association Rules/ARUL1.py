#! /usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 24 15:21:29 2021

@author: Bea Jimenez <bea.jimenez@alumni.ie.edu>
"""

import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules
from mlxtend.preprocessing import TransactionEncoder


data = pd.read_csv("association_rules_20000_fullBinaryVectors.csv", header=None)

data.head()

data = data.set_index(0)


data.columns = ["Product" + str(i) for i in range(1, data.shape[1] + 1)]


sup = 0.045
lift = 4
frequent_itemsets = apriori(data, min_support=sup, use_colnames=True)
frequent_itemsets.sort_values(by="support", ascending=False)

association_rules(frequent_itemsets, metric="lift", min_threshold=lift).sort_values(
    by="lift", ascending=False
)

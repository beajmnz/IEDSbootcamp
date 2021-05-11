#! /usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 10 17:13:26 2021

@author: Bea Jimenez <bea.jimenez@alumni.ie.edu>
"""

"""
For Boston data:
1. show the names of the variables and a brief summary of them
2. extract the first 10 rows
3. extract the rows 4 th and 5 th with the last 4 variables
4. extract the rows with AGE bigger than 95. How many rows are they?
5. extract the rows 2 and 3 for the variables DIS, RAD and TAX
6. erase the columns B and LSTAT
7. replace the maximum value on DIS by 1
"""

import pandas as pd
from sklearn.datasets import load_boston
dataset = load_boston()
df = pd.DataFrame(dataset.data, columns = dataset.feature_names)


# 1. show the names of the variables and a brief summary of them
df.describe()

# 2. extract the first 10 rows
df.head(10)

# 3. extract the rows 4 th and 5 th with the last 4 variables
df.iloc[4:6,:].iloc[:,-4:]

# 4. extract the rows with AGE bigger than 95. How many rows are they?
df.loc[df.AGE>95,:]
df.loc[df.AGE>95,:].shape[0]

# 5. extract the rows 2 and 3 for the variables DIS, RAD and TAX
df.iloc[2:4,:].loc[:,["DIS","RAD","TAX"]]

# 6. erase the columns B and LSTAT
df.drop(columns=["B","LSTAT"])

# 7. replace the maximum value on DIS by 1
df.iloc[df.DIS.idxmax(),:].DIS = 1




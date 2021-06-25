#! /usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 23 13:07:59 2021

@author: Bea Jimenez <bea.jimenez@alumni.ie.edu>
"""

"""
Taking in consideration the iris dataset:
1. How many principal components can we consider?
2. How do you think is going to be the cumulated percentage of explained variance
attending to the number of components? Calculate it.
3. Consider the necessary number of components to explain at least a 99% of the
variance. Give the equations to calculate these components.
4. Calculate the new values for this decomposition and plot them.
5. Repeat the steps 3 and 4 taking a 95% of the variance.
"""

from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from sklearn import datasets
import sklearn.metrics as sm
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

iris = datasets.load_iris()
df = pd.DataFrame(iris.data)
df.head()
df.columns = ["Sepal_Length", "Sepal_Width", "Petal_Length", "Petal_Width"]

# 1. How many principal components can we consider?
df.shape[1]

# 2. How do you think is going to be the cumulated percentage of explained
# variance attending to the number of components? Calculate it.

pca = PCA(n_components=4)

pca.fit(df)

pca.explained_variance_ratio_
# array([0.92461872, 0.05306648, 0.01710261, 0.00521218])

# 3. Consider the necessary number of components to explain at least a 99% of the
# variance. Give the equations to calculate these components.

cum_sum = np.cumsum(pca.explained_variance_ratio_)
n_components = np.where(cum_sum >= 0.99)[0][0] + 1


# array([0.92461872, 0.97768521, 0.99478782, 1.        ])

# we need three components to get to 99%

pca.components_

# 4. Calculate the new values for this decomposition and plot them.

pca = PCA(n_components=3)
pca.fit(df)
data_pca = pd.DataFrame(pca.transform(df))

# run the following two lines at the same time
ax = plt.axes(projection="3d")
ax.scatter3D(data_pca[0], data_pca[1], data_pca[2], c=iris.target, cmap="Dark2")

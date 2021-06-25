#! /usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 23 17:21:44 2021

@author: Bea Jimenez <bea.jimenez@alumni.ie.edu>
"""

"""
Taking in consideration the previous digits dataset:
1. Which is the amount of variance explained taking only 2 principal components?
2. Calculate the new values for this decomposition.
3. Plot all the digits registers using these 2 principal components giving the color for
each target.
"""

from sklearn.datasets import load_digits
from plotnine import *
import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import plotly.express as px


digits = load_digits()
data = pd.DataFrame(digits.data)
data.shape

target = digits.target
data.head()

pca = PCA(2)
pca = pca.fit(data)

pca.explained_variance_ratio_
cum_sum = np.cumsum(pca.explained_variance_ratio_)

cum_sum[-1]

data_pca = pd.DataFrame(pca.transform(data))

(
    ggplot(aes(x=data_pca[0], y=data_pca[1], color=digits.target.astype(object)))
    + geom_point()
)


pca3 = PCA(3)
pca3 = pca3.fit(data)

pca3.explained_variance_ratio_
cum_sum3 = np.cumsum(pca3.explained_variance_ratio_)

cum_sum3[-1]

data_pca3 = pd.DataFrame(pca3.transform(data))


# run the following two lines at the same time
ax = plt.axes(projection="3d")
ax.scatter3D(
    data_pca3[0],
    data_pca3[1],
    data_pca3[2],
    c=digits.target.astype(object),
    cmap="Dark2",
)


# fig = px.scatter_3d(pictures, x='coord_x', y='coord_y', z='coord_z', color='target')
fig = px.scatter_3d(data_pca3, x=0, y=1, z=2, color=digits.target.astype(object))
fig.write_html("digits.html")

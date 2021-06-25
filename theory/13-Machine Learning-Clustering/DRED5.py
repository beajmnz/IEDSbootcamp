#! /usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 24 12:53:21 2021

@author: Bea Jimenez <bea.jimenez@alumni.ie.edu>
"""

from sklearn.datasets import load_digits
from plotnine import *
import pandas as pd
import numpy as np
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import plotly.express as px


digits = load_digits()
data = pd.DataFrame(digits.data)
data.shape

target = digits.target
data.head()


lda = LinearDiscriminantAnalysis(n_components=2)
lda.fit(data, digits.target)

data_lda = pd.DataFrame(lda.transform(data))

(
    ggplot(aes(x=data_lda[0], y=data_lda[1], color=digits.target.astype(object)))
    + geom_point()
)


lda3 = LinearDiscriminantAnalysis(n_components=3)
lda3.fit(data, digits.target)

data_lda3 = pd.DataFrame(lda.transform(data))


# run the following two lines at the same time
ax = plt.axes(projection="3d")
ax.scatter3D(
    data_lda3[0],
    data_lda3[1],
    data_lda3[2],
    c=digits.target.astype(object),
    cmap="Dark2",
)

fig = px.scatter_3d(data_lda3, x=0, y=1, z=2, color=digits.target.astype(object))
fig.write_html("digits_lda.html")

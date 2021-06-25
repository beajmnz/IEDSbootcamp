#! /usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 21 15:04:18 2021

@author: Bea Jimenez <bea.jimenez@alumni.ie.edu>
"""

from sklearn.cluster import KMeans
from sklearn import datasets
import sklearn.metrics as sm
import pandas as pd
from plotnine import *

iris = datasets.load_iris()
df = pd.DataFrame(iris.data)
df.head()
df.columns = ["Sepal_Length", "Sepal_Width", "Petal_Length", "Petal_Width"]

ggplot(aes(x="Sepal_Length", y="Sepal_Width"), df) + geom_point()
ggplot(aes(x="Petal_Length", y="Petal_Width"), df) + geom_point()

df.Petal_Length.corr(df.Petal_Width)


model = KMeans(n_clusters=3)
aux = df.loc[:, ["Sepal_Length", "Sepal_Width", "Petal_Length", "Petal_Width"]]
model.fit(aux)
modelLabels = model.labels_
modelCenters = model.cluster_centers_
df["Cluster"] = pd.Series(modelLabels, index=df.index)

df.groupby(by="Cluster").mean()

df.Cluster.value_counts()

ggplot(aes(x="Sepal_Length", y="Sepal_Width", color="Cluster"), df) + geom_point()
ggplot(aes(x="Petal_Length", y="Petal_Width", color="Cluster"), df) + geom_point()


new_flowers = pd.DataFrame(
    data={
        "Sepal_Length": [5, 6, 1, 2, 1],
        "Sepal_Width": [3, 3, 1, 2, 1],
        "Petal_Length": [5, 6, 1, 2, 1],
        "Petal_Width": [0.2, 0.1, 3, 4, 5],
    }
)

predictions = model.predict(new_flowers)
predictions

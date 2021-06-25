#! /usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 22 09:41:21 2021

@author: Bea Jimenez <bea.jimenez@alumni.ie.edu>
"""


"""
Try to calculate the optimal number of clusters by yourself for the Pokemon dataset 
using the variables "Speed", "Attack" and "Deffense" using the Silhouette criterion

"""


from plotnine import *
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score


pokemons = pd.read_excel("./Pokemon_description_filtered.xlsx")

sil_sc = []

for k in range(2, 20):  # remember to start at 2
    km = KMeans(n_clusters=k)
    km.fit(pokemons.loc[:, ["Speed", "Attack", "Defense"]])
    labels = km.labels_
    sil_sc.append(
        silhouette_score(pokemons.loc[:, ["Speed", "Attack", "Defense"]], labels)
    )

optimal_cluster = pd.DataFrame(
    {"Number of clusters": range(2, 20), "Silhouette score": sil_sc}
)

(
    ggplot(aes(x="Number of clusters", y="Silhouette score"), optimal_cluster)
    + geom_line()
    + geom_point()
)

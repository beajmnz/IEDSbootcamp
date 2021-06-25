#! /usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 22 09:14:30 2021

@author: Bea Jimenez <bea.jimenez@alumni.ie.edu>
"""

"""
Try to calculate the optimal number of clusters by yourself for the Pokemon dataset 
using the variables "Speed", "Attack" and "Deffense" using the Elbow criterion

"""


from plotnine import *
import pandas as pd
from sklearn.cluster import KMeans


pokemons = pd.read_excel("./Pokemon_description_filtered.xlsx")


inertia = []

for k in range(1, 10):
    km = KMeans(n_clusters=k)
    km.fit(pokemons.loc[:, ["Speed", "Attack", "Defense"]])
    inertia.append(km.inertia_)

optimal_cluster = pd.DataFrame(
    {"Number of clusters": range(1, 10), "Distortion": inertia}
)

(
    ggplot(aes(x="Number of clusters", y="Distortion"), optimal_cluster)
    + geom_line()
    + geom_point()
    + ylim(0, 3000000)
)

#! /usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 21 15:39:51 2021

@author: Bea Jimenez <bea.jimenez@alumni.ie.edu>
"""

"""
Do a Kmeans analysis considering the Speed, Attack and Defense variables for the 
pokemons dataset. Take 5 clusters.
"""

from sklearn.cluster import KMeans
from sklearn import datasets
import sklearn.metrics as sm
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

pokemons = pd.read_excel("./Pokemon_description_filtered.xlsx")

pokemons_Type1 = pd.get_dummies(pokemons.Type1)
pokemons = pd.concat([pokemons, pokemons_Type1], axis=1)
pokemons_Legendary = pd.get_dummies(pokemons.Legendary)
pokemons = pd.concat([pokemons, pokemons_Legendary], axis=1)
pokemons_Generation = pd.get_dummies(pokemons.Generation)
pokemons = pd.concat([pokemons, pokemons_Generation], axis=1)


pokemodel = KMeans(n_clusters=5)
aux = pokemons.loc[:, ["Speed", "Attack", "Defense"]]
pokemodel.fit(aux)
modelLabels = pokemodel.labels_
modelCenters = pokemodel.cluster_centers_

pokemons["Cluster"] = pd.Series(modelLabels, index=pokemons.index)

pokemons.Cluster.value_counts()

# run the following two lines at the same time
ax = plt.axes(projection="3d")
ax.scatter3D(
    pokemons.Defense, pokemons.Attack, pokemons.Speed, c=pokemons.Cluster, cmap="YlGnBu"
)

res = pokemons.drop(["Generation", "Legendary"], axis=1)
res = res.iloc[:, 1:].groupby(by="Cluster").mean()
res.to_excel("./Clustered_pokemons.xlsx")

#! /usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 22 10:55:41 2021

@author: Bea Jimenez <bea.jimenez@alumni.ie.edu>
"""

"""
Do a dendrogram and agglomerative analysis with 20 pokemons and using the 
Defense, Attack and Speed variables
"""

from plotnine import *
import pandas as pd
from scipy.cluster import hierarchy

pokemons = pd.read_excel("./Pokemon_description_filtered.xlsx")

Twenty_pokemons = pokemons.sample(20)

z = hierarchy.linkage(
    Twenty_pokemons.loc[:, ["Speed", "Attack", "Defense"]],
    method="single",
    metric="euclidean",
)

dendogram = hierarchy.dendrogram(
    z,
    truncate_mode="lastp",
    p=10,
    leaf_font_size=9,
    leaf_rotation=45,
    labels=Twenty_pokemons.Name.values,
    color_threshold=(70),
    above_threshold_color="#AAAAAA",
)

labels = hierarchy.fcluster(z, 3, criterion="maxclust")

pokemons["Cluster"] = labels

pokemons.Cluster.value_counts()

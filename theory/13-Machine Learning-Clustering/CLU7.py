#! /usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 22 11:19:02 2021

@author: Bea Jimenez <bea.jimenez@alumni.ie.edu>
"""

"""
For the first 10k diamonds from the diamonds dataset and taking the clustering 
variables "price", "depth" and "x":
1. Determine the N optimal number of clusters attending to Silhouette criteria.
2. Do a segmentation analysis for all the variables with these N clusters and using 
these 3 clustering variables.
3. Obtain the labels for the diamonds doing an agglomerative analysis with N 
clusters and the 3 variables
4. Show a dendrogram showing the info for these N clusters
"""

from plotnine.data import diamonds
from plotnine import *
import pandas as pd
from scipy.cluster import hierarchy
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score


tenk_diamonds = diamonds.head(10000)

# 1. Determine the N optimal number of clusters attending to Silhouette criteria.

sil_sc = []

for k in range(2, 20):  # remember to start at 2
    km = KMeans(n_clusters=k)
    km.fit(tenk_diamonds.loc[:, ["price", "depth", "x"]])
    labels = km.labels_
    sil_sc.append(
        silhouette_score(tenk_diamonds.loc[:, ["price", "depth", "x"]], labels)
    )

optimal_cluster = pd.DataFrame(
    {"Number of clusters": range(2, 20), "Silhouette score": sil_sc}
)

(
    ggplot(aes(x="Number of clusters", y="Silhouette score"), optimal_cluster)
    + geom_line()
    + geom_point()
)

# 2. Do a segmentation analysis for all the variables with these N clusters
# and using these 3 clustering variables.


diam_model = KMeans(n_clusters=2)
aux = tenk_diamonds.loc[:, ["price", "depth", "x"]]
diam_model.fit(aux)
modelLabels = diam_model.labels_
modelCenters = diam_model.cluster_centers_

tenk_diamonds["Cluster"] = pd.Series(modelLabels, index=tenk_diamonds.index)

tenk_diamonds.Cluster.value_counts()


# 3. Obtain the labels for the diamonds doing an agglomerative analysis with N
# clusters and the 3 variables


# 4. Show a dendrogram showing the info for these N clusters

z = hierarchy.linkage(
    tenk_diamonds.loc[:, ["price", "depth", "x"]],
    method="single",
    metric="euclidean",
)

dendogram = hierarchy.dendrogram(
    z,
    truncate_mode="lastp",
    p=7,
    leaf_font_size=9,
    leaf_rotation=45,
    color_threshold=(70),
    above_threshold_color="#AAAAAA",
)

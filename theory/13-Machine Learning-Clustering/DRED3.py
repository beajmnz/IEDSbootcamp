#! /usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 23 17:11:02 2021

@author: Bea Jimenez <bea.jimenez@alumni.ie.edu>
"""

"""
The digits dataset contains 1.797 images with size 8x8 with numbers from 0 to 9.
Taking in consideration this dataset:
1. How many principal components are required to explain at least a 45% of the
variance?
2. Calculate the new values for this decomposition. Which are the equations to
calculate these new coordinates?
"""

from sklearn.datasets import load_digits
import matplotlib as plt
import pandas as pd
import numpy as np
from sklearn.decomposition import PCA

digits = load_digits()
data = pd.DataFrame(digits.data)
data.shape

target = digits.target
data.head()

plt.imshow(np.array(data.iloc[50, :]).reshape(8, 8))
np.array(data.iloc[50, :].reshape(8, 8))


pca = PCA(0.45)
pca = pca.fit(data)
pca.n_components_

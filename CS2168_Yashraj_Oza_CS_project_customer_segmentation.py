# -*- coding: utf-8 -*-
"""Customer Segmentation.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1o5qwl1XDjKxadIFWnTW90GSJYtfLig-j
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('Mall_Customers.csv')

df.head(10)

df.tail(8)

df.shape

df.info()

X = df.iloc[:,[3,4]].values

X

from sklearn.cluster import KMeans
wcss =[]

"""By using Elbow method"""

for i in range(1,11):
  kmeans = KMeans(n_clusters=i, init='k-means++',random_state=0)
  kmeans.fit(X)
  wcss.append(kmeans.inertia_)

plt.plot(range(1,11), wcss)
plt.title('The elbow method')
plt.xlabel('No. of clusters')
plt.ylabel('WCSS values')
plt.show()

"""By using K-means"""

kmeansmodel = KMeans(n_clusters = 5, init= 'kmean++', random_state = 0)

y_kmeans = kmeans.fit_predict(X)

plt.scatter(X[y_kmeans == 0,0], X[y_kmeans == 0,1], s=80, c= "red", label='Customer 1' )
plt.scatter(X[y_kmeans == 1,0], X[y_kmeans == 1,1], s=80, c= "blue", label='Customer 2' )
plt.scatter(X[y_kmeans == 2,0], X[y_kmeans == 2,1], s=80, c= "green", label='Customer 3' )
plt.scatter(X[y_kmeans == 3,0], X[y_kmeans == 3,1], s=80, c= "yellow", label='Customer 4' )
plt.scatter(X[y_kmeans == 4,0], X[y_kmeans == 4,1], s=80, c= "orange", label='Customer 5' )
plt.scatter(kmeans.cluster_centers_[:,0], kmeans.cluster_centers_[:,1], s=100, c= 'magenta', label= 'centroids')
plt.title('Clusters of customers')
plt.xlabel('Annual Income (k$)')
plt.ylabel('Spending Score (1-100)')
plt.legend()
plt.show()


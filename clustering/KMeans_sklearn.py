import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns; sns.set
import matplotlib
from sklearn.cluster import KMeans

# 4 drops generating
from sklearn.datasets import make_blobs
X, y_true = make_blobs(n_samples = 400, centers = 4, cluster_std = 0.60, random_state = 0)

matplotlib.use("TkAgg")
plt.scatter(X[:, 0], X[:, 1], s = 20)
plt.show()

# creation of 4 classes, training, predict
kmeans = KMeans(n_clusters=4)
kmeans.fit(X)
y_kmeans = kmeans.predict(X)

# build and visualise cluster centres
from sklearn.datasets import make_blobs
X, y_true = make_blobs(n_samples = 400, centers = 4, cluster_std = 0.60, random_state = 0)

# visualise
plt.scatter(X[:, 0], X[:, 1], c = y_kmeans, s = 20, cmap  = 'summer')
centers = kmeans.cluster_centers_
plt.scatter(centers[:, 0], centers[:, 1], c = 'blue', s = 100, alpha=0.9)
plt.show()
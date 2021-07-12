
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans


# make_blobs is a way to randomly generate clustered data
data = make_blobs(n_samples=200, n_features=2, centers=4, cluster_std=1.8, random_state=101)


# can set the cluster numbers variably
kmeans = KMeans(n_clusters=4)
kmeans.fit(data[0])
# kmeans.labels_
# kmeans.cluster_centers_

fig, (ax1, ax2) = plt.subplots(1, 2, sharey=True, figsize=(10,6))
ax1.set_title('K Means')
ax1.scatter(data[0][:, 0], data[0][:, 1], c=kmeans.labels_)
ax2.set_title('Original')
ax2.scatter(data[0][:, 0], data[0][:, 1], c=data[1])

plt.show()

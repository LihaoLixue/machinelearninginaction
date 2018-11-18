from scipy.io import loadmat
import numpy as np
from Ch02.wuenda.find_closet import find_closest_centroids, compute_centroids, run_k_means
import matplotlib.pyplot as plt
data = loadmat('ex7data2.mat')
X = data['X']
initial_centroids = np.array([[3, 3], [6, 2], [8, 5]])

# idx = find_closest_centroids(X, initial_centroids)



# a = compute_centroids(X, idx, 3)
# print(a)
idx, centroids = run_k_means(X, initial_centroids, 10)
cluster1 = X[np.where(idx == 0)[0],:]
cluster2 = X[np.where(idx == 1)[0],:]
cluster3 = X[np.where(idx == 2)[0],:]

fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_title('Scatter Plot')
plt.xlabel('X')
plt.ylabel('Y')

# fig,ax = plt.subplots(figsize=(12,8),ncols=1,nrows=1)
ax.scatter(cluster1[:,0], cluster1[:,1], s=30, color='r', label='Cluster 1')
ax.scatter(cluster2[:,0], cluster2[:,1], s=30, color='g', label='Cluster 2')
ax.scatter(cluster3[:,0], cluster3[:,1], s=30, color='b', label='Cluster 3')
plt.legend('"Cluster1",Cluster2,Cluster 3')
plt.show()
# ax.legend()
from scipy.io import loadmat
import numpy as np
import matplotlib.pyplot as plt

from Ch02.wuenda.find_closet import init_centroids, run_k_means, find_closest_centroids

image_data = loadmat('bird_small.mat')
print(image_data)
A = image_data['A']
print(A.shape)
A = A / 255.

# reshape the array
X = np.reshape(A, (A.shape[0] * A.shape[1], A.shape[2]))

# randomly initialize the centroids
initial_centroids = init_centroids(X, 16)

# run the algorithm
idx, centroids = run_k_means(X, initial_centroids, 10)

# get the closest centroids one last time
idx = find_closest_centroids(X, centroids)

# map each pixel to the centroid value
X_recovered = centroids[idx.astype(int),:]

# reshape to the original dimensions
X_recovered = np.reshape(X_recovered, (A.shape[0], A.shape[1], A.shape[2]))
fig, axes = plt.subplots(1, 2, figsize=(12,6))
# plt.imshow(A)
# plt.show()
axes[0].imshow(A)
axes[1].imshow(X_recovered)
plt.show()
# plt.imshow(X_recovered)
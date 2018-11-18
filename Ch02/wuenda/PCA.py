from scipy.io import loadmat
import numpy as np
import matplotlib.pyplot as plt
mat = loadmat('ex7data1.mat')
X = mat['X']
print(X.shape)
plt.scatter(X[:,0], X[:,1], facecolors='none', edgecolors='b')
plt.show()
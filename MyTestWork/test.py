import cv2
import matplotlib.pyplot as plt
import numpy as np
# https://blog.csdn.net/llh_1178/article/details/73321075
img = cv2.imread('abc.jpg', 0)  # image read be 'gray'
plt.subplot(221), plt.imshow(img, 'gray'), plt.title('original')
plt.xticks([]), plt.yticks([])

# 改变图像的维度
img1 = img.reshape((img.shape[0] * img.shape[1], 1))
img1 = np.float32(img1)

# 设定一个criteria，
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)

# 设定一个初始类中心flags
flags = cv2.KMEANS_RANDOM_CENTERS
# 应用K-means
compactness, labels, centers = cv2.kmeans(img1, 2, None, criteria, 5, flags)
compactness_1, labels_1, centers_1 = cv2.kmeans(img1, 2, None, criteria, 10, flags)
compactness_2, labels_2, centers_2 = cv2.kmeans(img1, 2, None, criteria, 15, flags)
img2 = labels.reshape((img.shape[0], img.shape[1]))
img3 = labels_1.reshape((img.shape[0], img.shape[1]))
img4 = labels_2.reshape((img.shape[0], img.shape[1]))
plt.subplot(222), plt.imshow(img2, 'gray'), plt.title('kmeans_attempts_5')
plt.xticks([]), plt.yticks([])
plt.subplot(223), plt.imshow(img3, 'gray'), plt.title('kmeans_attempts_10')
plt.xticks([]), plt.yticks([])
plt.subplot(224), plt.imshow(img4, 'gray'), plt.title('kmeans_attempts_15')
plt.xticks([]), plt.yticks([])
plt.savefig("kmeans_attempts.png")
plt.show()

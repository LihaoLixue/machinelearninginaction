import tensorflow as tf
import numpy as np
import cv2
import matplotlib.pyplot as plt
# https://blog.csdn.net/llh_1178/article/details/73321075
# from tensorflow.examples.tutorials.mnist import input_data
img = cv2.imread("water_coins.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# 将颜色转变为灰色之后，可为图像设一个阈值，将图像二值化。
ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
# 下面用morphologyEx变换来除去噪声数据，这是一种对图像进行膨胀之后再进行腐蚀的操作，它可以提取图像特征：
kernel = np.ones((3,3), np.uint8)
opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations= 2)
# 通过对morphologyEx变换之后的图像进行膨胀操作，可以得到大部分都是背景的区域：
sure_bg = cv2.dilate(opening, kernel, iterations=3)
# 接着通过distanceTransform来获取确定前景区域，原理是应用一个阈值来决定哪些区域是前景，越是远离背景区域的边界的点越可能属于前景。
dist_transform = cv2.distanceTransform(opening, cv2.DIST_L2, 5)
ret, sure_fg = cv2.threshold(dist_transform, 0.7 * dist_transform.max(), 255, 0)
# 考虑前景和背景中有重合的部分，通过sure_fg和sure_bg的集合相减得到。
sure_fg = np.uint8(sure_fg)
unknown = cv2.subtract(sure_bg, sure_fg)
# 现在有了这些区域，就可以设定“栅栏”来阻止水汇聚了，这通过connectedComponents函数来完成
ret, markers = cv2.connectedComponents(sure_fg)
# 在背景区域上加1， 这会将unknown区域设置为0：
markers = markers + 1
markers[unknown==255] = 0
# 最后打开门，让水漫起来并把栅栏绘成红色
markers = cv2.watershed(img, markers)
img[markers == -1] = [255, 0, 0]
plt.imshow(img), plt.xticks([]),plt.yticks([])
plt.show()

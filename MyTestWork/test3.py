import numpy as np
import cv2
from matplotlib import pyplot as plt
# https://blog.csdn.net/llh_1178/article/details/73321075

# 首先加载图片，然后创建一个与所加载图片同形状的掩模，并用0填充。
img = cv2.imread("abc.jpg")
mask = np.zeros(img.shape[:2], np.uint8)

# 然后创建以0填充的前景和背景模型：
bgdModel = np.zeros((1, 65), np.float64)
fgdModel = np.zeros((1, 65), np.float64)
# 在实现GrabCut算法前，先用一个标识出想要隔离的对象的矩形来初始化它，这个矩形我们用下面的一行代码定义（x,y,w,h）：
rect = (100, 50, 421, 378)
# 接下来用指定的空模型和掩摸来运行GrabCut算法
# mask, bgdModel, fgdModel = cv2.grabCut(img,mask,None,bgdModel,fgdModel,5,cv2.GC_INIT_WITH_MASK)
cv2.grabCut(img, mask, rect, bgdModel, fgdModel, 5, cv2.GC_INIT_WITH_RECT)  # 5是指算法的迭代次数。
# 然后，我们再设定一个掩模，用来过滤之前掩模中的值（0-3）。值为0和2的将转为0，值为1和3的将转化为1，这样就可以过滤出所有的0值像素（背景）。
mask2 = np.where((mask == 2) | (mask == 0), 0, 1).astype("uint8")
img = img * mask2[:, :, np.newaxis]
# 最后可视化展现分割前后的图像
plt.subplot(1, 2, 1)
plt.imshow(img)
plt.title("grabcut"), plt.xticks([]), plt.yticks([])

plt.subplot(1, 2, 2)
plt.imshow(cv2.imread("abc.jpg"))
plt.title("original"), plt.xticks([]), plt.yticks([])
plt.savefig("grabcut.png")

import Ch07.adaboost as adaboot
from numpy import *
#https://www.cnblogs.com/liuq/p/9927580.html
#https://blog.csdn.net/taichitaichi/article/details/80445013
datMat,classLabels=adaboot.loadSimpData()
# D = mat(ones((5, 1)) / 5)
# a,b,c=adaboot.buildStump(datMat,classLabels,D)
a = adaboot.adaBoostTrainDS(datMat,classLabels,9)
print(a)

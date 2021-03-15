from Ch10 import kMeans
from numpy import *
dataMat=kMeans.loadDataSet('testSet2.txt')
print(shape(dataMat))
a=mat(dataMat)
# b,c = kMeans.kMeans(a,3)
b,c=kMeans.biKmeans(a,3)
kMeans
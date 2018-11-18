import kMeans
from numpy import *
dataMat=kMeans.loadDataSet('testSet2.txt')
print(shape(dataMat))
a=mat(dataMat)
b,c=kMeans.biKmeans(a,3)

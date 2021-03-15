from Ch06 import svmMLiA

a,b = svmMLiA.loadDataSet('testSet.txt')
#a:数据集，b:类标签；0.6：常数C;0.001:容错率；40取消前最大数
# d,error=svmMLiA.smoP(a,b,0.6,0.001,40)
# print(d)
# print(error)
svmMLiA.testDigits()
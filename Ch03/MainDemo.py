from Ch03 import trees


myData,labels=trees.createDataSet()
# c1 = trees.chooseBestFeatureToSplit(myData)
d1 = trees.createTreeOfEntroy(myData,labels)
print(d1)
# treePlotter.createPlot(d1)

# a=treePlotter.retrieveTree(0)
# treePlotter.createPlot()
# b = treePlotter.getNumLeafs(a)
# c = treePlotter.getTreeDepth(a)
#
# trees.classify(b,labels,[1,1])
# len = treePlotter.getNumLeafs(b)
# print(len)
# ceng = treePlotter.getTreeDepth(b)
# print(ceng)
# treePlotter.createPlot(b)
# d=trees.classify(b,labels,[1,0])
# print(d)


# 信息增益
# myData,labels=trees.createDataSet()
# c2 = trees.chooseBestFeatureToSplitOfRito(myData)
# print(c2)
# d2= trees.createTreeOfRito(myData,labels)
# print(d2)
# treePlotter.createPlot(d2)
#
# # #Gini系数
# myData,labels=trees.createDataSet()
# c3 = trees.chooseBestFeatureToSplitOfGini(myData)
# print(c3)
# d3= trees.createTreeOfGini(myData,labels)
# print(d3)
# treePlotter.createPlot(d3)

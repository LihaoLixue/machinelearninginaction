from Ch03 import trees, treePlotter
from Ch03.treePlotter import getNumLeafs

myData,labels=trees.createDataSet()
# a= trees.calcShannonEnt(myData)
# print(a)
# b = trees.splitDataSet(myData,0,1)
# c = trees.chooseBestFeatureToSplit(myData)
a= trees.createTree(myData,labels)
# print(a)
# treePlotter.createPlot()
b = getNumLeafs(a)
print(b)

# b=treePlotter.retrieveTree(0)
# trees.classify(b,labels,[1,1])
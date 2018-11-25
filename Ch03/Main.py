from Ch03 import trees, treePlotter

myData,labels=trees.createDataSet()
# a= trees.calcShannonEnt(myData)
# print(a)
# trees.splitDataSet(myData,0,1)
# trees.chooseBestFeatureToSplit(myData)
# a= trees.createTree(myData,labels)
b=treePlotter.retrieveTree(0)
trees.classify(b,labels,[1,1])
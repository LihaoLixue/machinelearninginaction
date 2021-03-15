from Ch09 import regTrees
import numpy as np
myData = regTrees.loadDataSet('ex00.txt')
myMat = np.mat(myData)
regTrees.createTree(myMat)

# coding: utf-8
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from Ch03 import trees, treePlotter
plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']
trainData = pd.read_csv("titanic/train.csv")
testData = pd.read_csv("titanic/test.csv")
trainData = np.array(trainData)
print(type(trainData))
labels = ['Pclass','Sex','Age','Embacked']
data=[]
for d in trainData:
    temp = []
    temp.append(str(d[2]))
    temp.append(str(d[4]))
    temp.append(str(d[5]))
    temp.append(str(d[11]))
    if d[1] == 1:
        temp.append('yes')
    else:
        temp.append('no')
    data.append(temp)
tree = trees.createTree(data,labels)
treePlotter.createPlot(tree)
print(tree)


'''决策树分类器
    参数：inputTree：构建的决策树，  
    featureLabels,testVec：测试数据的特征标签和特征值
'''
def classify(inputTree,featureLabels,testVec):
    firstStr = list(inputTree.keys())[0]
    secondDict = inputTree[firstStr]
    featureIndex = featureLabels.index(firstStr)
    for key in secondDict.keys():
        if testVec[featureIndex] == key:
            global classLabel
            if isinstance(secondDict[key],dict):
                classLabel = classify(secondDict[key],featureLabels,testVec)
            else:
                classLabel = secondDict[key]
    return classLabel

'''预测'''
testData = np.array(testData)
featureLabels = ['Pclass','Sex','Age','Embacked']
count=0
for test in testData:
    temp = []
    temp.append(str(test[1]))
    temp.append(str(test[3]))
    temp.append(str(test[4]))
    temp.append(str(test[10]))
    if test[1] == 1:
        temp.append('yes')
    else:
        temp.append('no')
    if classify(tree,featureLabels,temp)==temp[4]:
        count=+1;
print(count/len(testData))




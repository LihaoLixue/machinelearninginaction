# coding: utf-8
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import random
plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']
trainData = pd.read_csv("titanic/train.csv")
testData = pd.read_csv("titanic/test.csv")
'''sex与Survived的关系'''
trainData = np.array(trainData)
aliveCount = [0,0]
deadCount = [0,0]
pos = [1,2]
for data in trainData:
    if data[4] == 'male':
        if data[1] == 1:
            aliveCount[1] += 1
        else:
            deadCount[1] += 1
    else:
        if data[1] == 1:
            aliveCount[0] += 1
        else:
            deadCount[0] += 1
print('sex dead ati: female is %0.3f%%, male is %0.3f%%' % (
deadCount[0] / (aliveCount[0]+deadCount[0]), deadCount[1] / (aliveCount[1]+deadCount[1])))
ax = plt.figure(figsize=(8,6)).add_subplot(111)
ax.bar(pos, deadCount, color='r', alpha=0.6, label='死亡')
ax.bar(pos, aliveCount, color='g', bottom=deadCount, alpha=0.6, label='幸存')
ax.legend(fontsize=16, loc='best')
ax.set_xticks(pos)
ax.set_xticklabels(['女性','男性'], size=15)
ax.set_title('性别和是否幸存的关系', size=20)
plt.show()


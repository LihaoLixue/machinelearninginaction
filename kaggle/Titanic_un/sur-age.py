# coding: utf-8
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import random
plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']
trainData = pd.read_csv("titanic/train.csv")
testData = pd.read_csv("titanic/test.csv")
'''处理年龄缺失'''
for i in range(len(trainData)):
    if np.isnan(trainData.iloc[i, 5]):
        trainData.iloc[i, 5] = random.randint(29 - 14, 29 + 14)
ageDis = {}
trainData = np.array(trainData)
for data in trainData:
    if data[5] not in ageDis.keys():
        ageDis[data[5]] = 0
    ageDis[data[5]] += 1
ageDis = sorted(ageDis.items(), key=lambda item: item[0])
age = []
ageCount = []
for d in ageDis:
    age.append(d[0])
    ageCount.append(d[1])
plt.bar(age, ageCount)
plt.title('年龄分布图')
plt.xlabel('年龄')
plt.ylabel('人数', verticalalignment='baseline', horizontalalignment='left')
plt.show()


'''年龄段划分'''
def life(age):
    if age >= 66:
        return 4    #老年
    else:
        if age >= 41:
            return 3  #中年
        else:
            if age >= 18:
                return 2 #青年
            else:
                if age >= 7:
                    return 1  #少年
                else:
                    return 0  #孩童


'''各年龄段的死亡和幸存人数'''
trainData = np.array(trainData)
aliveCount = [0,0,0,0,0]
deadCount = [0,0,0,0,0]
for data in trainData:
    if data[1] == 1:
        aliveCount[life(data[5])] += 1
    else:
        deadCount[life(data[5])] += 1
pos = [1,2,3,4,5]
print('age dead ati: 儿童 is %0.3f%%, 少年 is %0.3f%%, 青年 is %0.3f%%, 中年 is %0.3f%%, 老年 is %0.3f%%' % (
deadCount[0] / (deadCount[0]+aliveCount[0]), deadCount[1] / (deadCount[1]+aliveCount[1]),
deadCount[2] / (deadCount[2]+aliveCount[2]),deadCount[3] / (deadCount[3]+aliveCount[3]),
deadCount[4] / (deadCount[4]+aliveCount[4])))
print('age alive ati: 儿童 is %0.3f%%, 少年 is %0.3f%%, 青年 is %0.3f%%, 中年 is %0.3f%%, 老年 is %0.3f%%' % (
aliveCount[0] / (deadCount[0]+aliveCount[0]), aliveCount[1] / (deadCount[1]+aliveCount[1]),
aliveCount[2] / (deadCount[2]+aliveCount[2]),aliveCount[3] / (deadCount[3]+aliveCount[3]),
aliveCount[4] / (deadCount[4]+aliveCount[4])))
ax = plt.figure(figsize=(8,6)).add_subplot(111)
ax.bar(pos, deadCount, color='r', alpha=0.6, label='死亡')
ax.bar(pos, aliveCount, color='g', bottom=deadCount, alpha=0.6, label='幸存')
ax.legend(fontsize=16, loc='best')
ax.set_xticks(pos)
ax.set_xticklabels(['孩童','少年','青年','中年','老年'], size=15)
ax.set_title('各年龄段的死亡和幸存人数', size=20)
plt.show()






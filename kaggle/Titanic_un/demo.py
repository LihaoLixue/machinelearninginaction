# coding: utf-8
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']
trainData = pd.read_csv("titanic/train.csv")
testData = pd.read_csv("titanic/test.csv")
trainData['Survived'].value_counts().polt.pie(autopct='%1.1f%%')
# plt.title("饼图示例-8月份家庭支出")
# plt.show()
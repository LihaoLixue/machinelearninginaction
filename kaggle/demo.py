# coding: utf-8
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from kaggle import treePlotter,trees
import random
plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']
trainData = pd.read_csv("titanic/train.csv")
testData = pd.read_csv("titanic/test.csv")
trainData['Survived'].value_counts().polt.pie(autopct='%1.1f%%')
# plt.title("饼图示例-8月份家庭支出")
# plt.show()
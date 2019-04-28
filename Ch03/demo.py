# coding: utf-8
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from Ch03 import trees, treePlotter
plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']
trainData = pd.read_csv("titanic/train.csv")
testData = pd.read_csv("titanic/test.csv")
print(trainData)
import numpy as np
import pandas as pd
import warnings
warnings.filterwarnings('ignore')
df = pd.read_csv('telecom_churn.csv')
print(df.shape)
# df['Churn'] = df['Churn'].astype('int64')
# print(df.describe())
# print(df.describe(include=['object', 'bool']))
# print(df['Churn'].value_counts())
print(df['Churn'].mean())
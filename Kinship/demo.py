# coding: utf-8
import matplotlib.pyplot as plt
from PIL import Image
import pandas as pd
import numpy as np
import os

train_df = pd.read_csv('data/scv/train_relationships.csv')
img_path = 'data/image/train'
print(os.listdir(os.path.join(img_path , train_df.p1[0])))
img_list = os.listdir(os.path.join(img_path , train_df.p1[0]))
fig,ax = plt.subplots(2,5, figsize=(50,20))
for i in range(len(img_list)):
    with open(os.path.join(img_path , train_df.p1[0] , img_list[i]),'rb') as f:
        img = Image.open(f)
        ax[i%2][i//2].imshow(img)
fig.show()

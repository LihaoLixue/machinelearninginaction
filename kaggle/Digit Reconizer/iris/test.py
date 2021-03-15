#载入数据集  
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import numpy as np
iris=load_iris()
iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
print(df.head())
df['is_train'] = np.random.uniform(0, 1, len(df)) <= .75
df['species'] = pd.Categorical(iris.target, iris.target_names)
print(df.head())

train, test = df[df['is_train']==True], df[df['is_train']==False]

features = df.columns[:4]
clf = RandomForestClassifier(n_jobs=2)
y, _ = pd.factorize(train['species'])
a = set(y)
clf.fit(train[features], y)

preds = iris.target_names[clf.predict(test[features])]
pd.crosstab(test['species'], preds, rownames=['actual'], colnames=['preds'])

instance=iris.data[[100,109]]
print(instance)
clf.predict(instance[[0]])
print('instance 0 prediction；',clf.predict(instance[[0]]))
print( 'instance 1 prediction；',clf.predict(instance[[1]]))
print(iris.target[100],iris.target[109])
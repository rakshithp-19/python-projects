

import matplotlib.pyplot as plt
from sklearn import datasets
import pandas as pd
import numpy as np

iris = datasets.load_iris()
X = pd.DataFrame(iris.data)
X.columns = ['Sepal_length','Sepal_width','Petal_length', 'Petal_width']

Y=pd.DataFrame(iris.target)
Y.columns = ['Targets']

plt.figure(figsize=(14,7))

colormap = np.array(['red','black','lime'])
plt.subplot(1,2,1)
plt.scatter(X.Petal_length,X.Petal_width, c=colormap[Y.Targets],s=40)
plt.title('Petals')

plt.figure(figsize=(14,7))

colormap = np.array(['red','black','lime'])
plt.subplot(1,2,1)
plt.scatter(X.Sepal_length,X.Sepal_width,c=colormap[Y.Targets],s=40)
plt.title('Real Classification')

plt.subplot(1,2,2)
plt.scatter(X.Petal_length,X.Petal_width, c=colormap[Y.Targets],s=40)
plt.title('K Means Classifaction')
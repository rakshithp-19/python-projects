from sklearn import preprocessing
from sklearn import datasets
import pandas as pd
import matplotlib.pyplot as plt

iris = datasets.load_iris()
X = pd.DataFrame(iris.data)
X.columns = ['sepal_length','sepal_width','petal_length','petal_width']

scaler = preprocessing.StandardScaler()
scaler.fit(X)
xsa = scaler.transform(X)
xs = pd.DataFrame(xsa,columns = X.columns)
xs.sample(5)

from sklearn.mixture import GaussianMixture

gmm = GaussianMixture(n_components=3)
gmm.fit(xs)

y_cluster_gmm = gmm.predict(xs)
plt.subplot(1,2,1)
plt.scatter(X.petal_length,X.petal_width,c=colormap[y_cluster_gmm],s=40)
plt.title('GMM Classification')
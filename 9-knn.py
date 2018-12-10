from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.datasets import load_iris
import numpy as np
iris_datasets = load_iris

print("\n FEATURE NAMES\ TARGET VALUES:\n", iris_dataset.target_names)
for i in range(len(iris_dataset.target_names)):
    print("\n [{0}]:[{1}]".format(i,iris_dataset.target_names[i]))

X_train,X_test,Y_train,Y_test = train_test_split(iris_dataset['data'],iris_dataset['target'],random_state=0)

kn = KNeighborsClassifier()
kn.fit(X_train,Y_train)

x_new = np.array([[5,2.9,1,0.2]])
print("\n XNEW:",x_new)

prediction = kn.predict(x_new)

print("PREDICTED TARGET VALUES:".format(prediction))
print("PREDICTED FEATURE NAMES:".format(iris_dataset['target_names'][prediction]))

i=1
x=X_test[i]
x_new = np.array([x])

for i in range(len(X_test)):
    x=X_test[i]
    x_new = np.array([x])
    prediction = kn.predict(x_new)
    print("ACTUAL VALUES: {0} {1}, PREDICTED VALUES: {2} {3}".format(y_test[i],iris_dataset['target_names'][y_test[i]],prediction,iris_dataset['target_names'][prediction]))
print("TEST SCORE(ACCURACY) : {:.2f}".format(kn.score(X_test,Y_test)))
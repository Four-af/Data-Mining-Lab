from sklearn import datasets
from sklearn.model_selection import train_test_split
import numpy as np
from P6 import DecisionTree

data = datasets.load_iris()
X, y = data.data, data.target

# print(data)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=1234
)

clf = DecisionTree(max_depth=10)
clf.fit(X_train, y_train)
predictions = clf.predict(X_test)

clf.print_dt()


def accuracy(y_test, y_pred):
    return np.sum(y_test == y_pred) / len(y_test)


acc = accuracy(y_test, predictions)
print(acc)

from sklearn import tree
from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

iris = load_iris()
x, y = iris.data, iris.target
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=123)


clf = tree.DecisionTreeClassifier()
clf = clf.fit(x, y)


clf.predict(x)


predictions = clf.predict(x)
accuracy_score(predictions, y)

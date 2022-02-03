from dagster import job, op
from sklearn import tree
from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split


@op
def load_train_test_set():
    iris = load_iris()
    x, y = iris.data, iris.target
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=123)
    return x_train, x_test, y_train, y_test


@op
def train_classifier(x, y):
    clf = tree.DecisionTreeClassifier()
    clf = clf.fit(x, y)
    return clf


@op
def classify(x, classifier):
    classifier.predict(x)


@op
def find_classifier_accuracy(x, y, classifier):
    predictions = classifier.predict(x)
    return accuracy_score(predictions, y)


@job
def basic_ml_job():
    x_train, x_test, y_train, y_test = load_train_test_set()
    classifier = train_classifier(x_train, y_train)
    classify(x_test, classifier)

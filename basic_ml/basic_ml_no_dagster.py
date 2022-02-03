from sklearn import tree
from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score


def load_train_test_set():
    iris = load_iris()
    return iris


def train_classifier(training_set):
    clf = tree.DecisionTreeClassifier()
    clf = clf.fit(training_set.data, training_set.target)
    return clf


def find_classifier_accuracy(training_set, classifier):
    predictions = classifier.predict(training_set.data)
    return accuracy_score(predictions, training_set.target)


if __name__ == "__main__":
    training_set = load_train_test_set()
    classifier = train_classifier(training_set)
    find_classifier_accuracy(training_set, classifier)

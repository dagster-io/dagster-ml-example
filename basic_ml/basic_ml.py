from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier

from dagster import get_dagster_logger, job, op

logger = get_dagster_logger()


@op
def load_train_test_set():
    iris = load_iris()
    return iris


@op
def train_classifier(training_set):
    clf = DecisionTreeClassifier()
    clf = clf.fit(training_set.data, training_set.target)
    return clf


@op
def find_classifier_accuracy(training_set, classifier):
    predictions = classifier.predict(training_set.data)
    logger.info(f"Accuracy: {accuracy_score(predictions, training_set.target)}")


@job
def basic_ml_job():
    training_set = load_train_test_set()
    classifier = train_classifier(training_set)
    find_classifier_accuracy(training_set, classifier)

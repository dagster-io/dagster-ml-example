from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

from dagster import get_dagster_logger, job, op

logger = get_dagster_logger()


@op
def load_train_test_set():
    iris = load_iris()
    return iris


@op
def train_classifier(training_set):
    """Trains a random forest classifier"""
    clf = RandomForestClassifier()
    clf = clf.fit(training_set.data, training_set.target)
    return clf


@op
def find_classifier_accuracy(training_set, classifier):
    predictions = classifier.predict(training_set.data)
    logger.info(f"Accuracy: {accuracy_score(predictions, training_set.target)}")


@job
def basic_ml_job():
    """Random forest version of basic ML job"""
    training_set = load_train_test_set()
    classifier = train_classifier(training_set)
    find_classifier_accuracy(training_set, classifier)

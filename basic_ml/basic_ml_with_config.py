from sklearn.datasets import load_iris, load_wine
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier

from dagster import get_dagster_logger, job, op

logger = get_dagster_logger()


@op(config_schema={"dataset": str})
def load_train_test_set(context):
    if context.op_config["dataset"] == "iris":
        return load_iris()
    elif context.op_config["dataset"] == "wine":
        return load_wine()
    else:
        raise ValueError()


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

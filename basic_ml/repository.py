from dagster import repository

from .basic_ml_with_config import basic_ml_job


@repository
def basic_ml():
    """
    The repository definition for this basic_ml Dagster repository.

    For hints on building your Dagster repository, see our documentation overview on Repositories:
    https://docs.dagster.io/overview/repositories-workspaces/repositories
    """
    return [basic_ml_job]

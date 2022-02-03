from dagster import repository

from basic_ml.jobs.say_hello import say_hello_job
from basic_ml.schedules.my_hourly_schedule import my_hourly_schedule
from basic_ml.sensors.my_sensor import my_sensor


@repository
def basic_ml():
    """
    The repository definition for this basic_ml Dagster repository.

    For hints on building your Dagster repository, see our documentation overview on Repositories:
    https://docs.dagster.io/overview/repositories-workspaces/repositories
    """
    jobs = [say_hello_job]
    schedules = [my_hourly_schedule]
    sensors = [my_sensor]

    return jobs + schedules + sensors

from basic_ml.jobs.say_hello import say_hello


def test_say_hello():
    """
    This is an example test for a Dagster job.

    For hints on how to test your Dagster graphs, see our documentation tutorial on Testing:
    https://docs.dagster.io/concepts/testing
    """
    result = say_hello.execute_in_process()

    assert result.success
    assert result.output_for_node("hello") == "Hello, Dagster!"

import setuptools

setuptools.setup(
    name="basic_ml",
    packages=setuptools.find_packages(exclude=["basic_ml_tests"]),
    install_requires=[
        "dagster==0.13.16",
        "dagit==0.13.16",
        "pytest",
    ],
)

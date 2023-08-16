from setuptools import find_packages, setup

setup(
    name="dagster_starter",
    packages=find_packages(exclude=["dagster_starter_tests"]),
    install_requires=[
        "dagster",
        "dagster-cloud",
        "pyGithub",
        "matplotlib",
        "pandas",
        "nbconvert",
        "nbformat",
        "ipykernel",
        "jupytext",
    ],
    extras_require={"dev": ["dagster-webserver", "pytest"]},
)

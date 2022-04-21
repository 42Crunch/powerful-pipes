from setuptools import setup

with open("requirements.txt", "r") as f:
    requirements = f.read().splitlines()

with open("requirements.performance.txt", "r") as f:
    requirements_performance = f.read().splitlines()

setup(
    install_requires=requirements
)

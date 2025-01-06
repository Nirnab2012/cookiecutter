from setuptools import find_packages, setup
from demo-project import __version__

setup(
    name="demo-project",
    packages=find_packages(exclude=["tests", "tests.*"]),
    setup_requires=["wheel"],
    version=__version__,
    description="cookiecutter demo",
    author="Nirnab",
)

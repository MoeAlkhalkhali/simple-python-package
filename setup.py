from setuptools import setup, find_packages
setup(
    name="SimplePythonPackage",
    version="0.0.1",
    packages=find_packages(),
    install_requires=[
        "cachetools==4.2.4"
])

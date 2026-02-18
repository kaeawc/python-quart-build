import os
from setuptools import setup, find_packages

setup(
    name='python-quart-build',
    version='0.0.1',
    description='Python quart Build',
    url='https://github.com/kaeawc/python-quart-build/',
    author='Jason Pearson',
    author_email='jason.d.pearson@gmail.com',
    license='MIT',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "coverage==7.13.4",
        "Delorean==1.0.0",
        "ipdb==0.13.13",
        "mock==5.2.0",
        "nose2==0.15.1",
        "numpy==2.2.6",
        "pycodestyle==2.14.0",
        "PyYaml==6.0.3",
        "quart-cors==0.8.0",
        "Quart==0.20.0",
        "requests==2.32.5",
        "tox==4.38.0",
    ],
    zip_safe=False)

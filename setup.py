import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "CurveFitting",
    version = "0.0.2",
    author = "Rob Beagrie",
    author_email = "rob@beagrie.com",
    description = ("A package containing some utilities for curve fitting in python."),
    license = "BSD",
    packages=['CurveFitting'],
    long_description=read('README'),
    install_requires=['numpy>=1.8.0', 'scipy>=0.13.0'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",
    ],
)

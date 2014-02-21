import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "an_example_project",
    version = "0.0.4",
    author = "hongjin.cao",
    author_email = "hognjin.cao@qunar.com",
    description = ("An demonstration of how to create, document, and publish "
                                   "a project"),
    license = "BSD",
    keywords = "example documentation tutorial",
    url = "http://gitlab.corp.qunar.com/hongjin.cao/newproject/tree/master",
    packages=['an_example_project'],
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",
    ],
)

# add some trash

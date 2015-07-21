# from distutils.core import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
import os
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

from setuptools import setup
setup(
    name='odl-learning-labs',
    description='OpenDaylight Application Development Learning Lab Scripts using Python and RESTCONF',
    version='1.0',
    packages=['basics', 'labs', 'settings', ],
    url='http://github.com/bencarle/odl-learning-labs',
    license='Apache License, Version 2.0',
    long_description=read('../README.md'),
    install_requires=[
        "requests",
        "ipaddress",
        "lxml",
        "logilab-common",
        "tabulate",
        "future",
        "pexpect",
    ],
)

import os
from setuptools import setup

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='ryanSort',
    version='0.1.0',
    packages=['ryanSort'],
    description='Various sorting algorithms for practice',
    author='Ryan Massoth',
    author_email='rmassoth82@gmail.com',
)

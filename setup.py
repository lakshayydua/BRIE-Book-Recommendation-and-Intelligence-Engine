"""
setup.py to provide streamlined package management.
To execute this program:
sudo pip install -e .
python setup.py clean
"""

from setuptools import setup, find_packages, Command
from codecs import open
from os import path, system

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


setup(

    name='BRIE',  # Required

    version='1.0.0',

    description='BRIE Github Repo',

    long_description=long_description,

    author='BRIE',

    packages=find_packages(exclude=['contrib', 'docs', 'tests']),  # Required

    install_requires = ['setuptools',
                        'django',
                        'pymysql',
                        'pymongo[tls,srv]',
                        'mysqlclient',
                        'plotly',
                        'numpy',
                        'pandas',
                        'pillow',
                        'nltk',
                        'gunicorn',
                        ],  # Optional


    # To export all data files (non .py files) inside utils directory.
    # Since utils contains __init__.py, a utils package directory will be created inside /usr/local/lib/python2.7
    # This allows data files such as config.json to be included in /usr/local/lib/python2.7/utils which is used by other programs
    
)
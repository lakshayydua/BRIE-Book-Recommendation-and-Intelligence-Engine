"""
setup.py to provide streamlined package management.
To execute this program:
sudo pip install -e .
python setup.py clean
"""

from setuptools import setup, find_packages, Command
from codecs import open
from os import path, system
import logging

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

class CleanCommand(Command):
    """Custom clean command to tidy up the project root."""
    user_options = []
    def initialize_options(self):
        pass
    def finalize_options(self):
        pass
    def run(self):
        system('rm -vrf ./dist ./*.pyc ./*.tgz ./*.egg-info')
        
setup(

    name='BRIE',  # Required

    version='1.0.0',

    description='BRIE Github Repo',

    long_description=long_description,

    author='BRIE',

    packages=find_packages(exclude=['contrib', 'docs', 'tests']),  # Required

    install_requires = ['setuptools==40.2.0',
                        'MySQL-python',
                        'django mysqlclient',
                        'django pymongo[tls,srv]==3.6.1',
                        'plotly'
                        'numpy',
                        'unicodecsv==0.14.1',
                        'anytree==2.4.3',
                        'pandas',
                        'nltk'
                        ],  # Optional


    # To export all data files (non .py files) inside utils directory.
    # Since utils contains __init__.py, a utils package directory will be created inside /usr/local/lib/python2.7
    # This allows data files such as config.json to be included in /usr/local/lib/python2.7/utils which is used by other programs
    package_data={'utils': ['*']},
    include_package_data=True,

    cmdclass={
            'clean': CleanCommand,
        }
)


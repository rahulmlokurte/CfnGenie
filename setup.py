from setuptools import setup, find_packages
from codecs import open
from os import path

path.abspath(path.dirname(__file__))

with open("README.md", encoding="utf-8") as f:
    long_description = f.read()

packages = find_packages()

setup(
    name='cfnGenie',
    version='0.1.0',
    description='CfnGenie is an open source command-line interface (CLI) tool that enables users to generate AWS'
                'CloudFormation templates from existing AWS resources',
    long_description=long_description,
    author='Rahul Lokurte',
    author_email='rahul.m.lokurte@gmail.com',
    url='https://github.com/rahulmlokurte/CfnGenie',
    packages=packages,
    entry_points={
        'console_scripts': [
            'cfnGenie = cfnGenie.cli:main',
        ],
    },
    install_requires=[
        'PyYAML==6.0', 'boto3==1.26.130', 'cookiecutter==2.1.1', 'click==8.1.3', 'rich==13.3.5'
    ],
)

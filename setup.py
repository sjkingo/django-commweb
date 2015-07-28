#!/usr/bin/env python

import os
from setuptools import setup, find_packages

from commweb import __version__

long_description = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-commweb',
    version=__version__,
    description='Django module for interfacing with the CommWeb merchant gateway.',
    long_description=long_description,
    author='Sam Kingston',
    author_email='sam@sjkwi.com.au',
    url='https://github.com/sjkingo/django-commweb',
    install_requires=['Django>=1.5', 'requests'],
    packages=find_packages(exclude=[]),
    include_package_data=True,
    license='BSD License',
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.4",
        "Environment :: Web Environment",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Framework :: Django",
    ],
)

import os
from distribute_setup import use_setuptools
use_setuptools()
from setuptools import setup

README = open(os.path.join(os.path.dirname(__file__), 'README')).read()

setup(
    name = "maillib",
    version = "0.1.2",
    description = "A simplified interface to Python's email package.",
    long_description = README,
    author = 'Joseph Kocherhans',
    author_email = 'jkocherhans@gmail.com',
    license='BSD',
    url='http://github.com/jkocherhans/maillib',
    packages = ['maillib'],
    classifiers = [
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Communications :: Email'
    ],
    test_suite='maillib.tests.all',
    install_requires=['chardet']
)

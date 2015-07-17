#!/usr/bin/env python

import ez_setup
import dnz
from setuptools import setup, find_packages
ez_setup.use_setuptools()

setup(
    name='dnz',
    packages=find_packages(),
    version=dnz.__version__,
    license=dnz.__license__,
    description='A python client for the DNZ API',
    long_description=open('README.md').read(),
    author=dnz.__author__,
    author_email='chris.mcdowall@gmail.com',
    url='https://github.com/fogonwater/pydnz',
    download_url='https://github.com/fogonwater/pydnz/tarball/0.1',
    keywords=['libraries', 'DNZ', 'DigitalNZ'],
    classifiers=[],
    install_requires=['requests'],
    extras_require={
        'tests': ['nose >= 1.0']
    }
)

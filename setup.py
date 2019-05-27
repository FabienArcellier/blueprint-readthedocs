#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

setup(
    name='blueprint_readthedocs',
    version='1.0',
    packages=find_packages(exclude=["tests", "tests.*"]),
    license='MIT',
    install_requires=[
    ],
    extras_require={
        'dev': [
            'sphinx'
        ]
    }
)

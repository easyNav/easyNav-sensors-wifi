#!/usr/bin/python
# -*- coding: utf-8 -*-

# This file is part of easyNav-sensors-wifi.
# https://github.com/easyNav/easyNav-sensors-wifi

# Licensed under the MIT license:
# http://www.opensource.org/licenses/MIT-license
# Copyright (c) 2014 Joel Tong me@joeltong.org


from setuptools import setup, find_packages
from easyNav_sensors_wifi import __version__

tests_require = [
    'mock',
    'nose',
    'coverage',
    'yanc',
    'preggy',
    'tox',
    'ipdb',
    'coveralls',
    'sphinx',
]

setup(
    name='easyNav-sensors-wifi',
    version=__version__,
    description='wifi sniffer to expose iwlist wifi info or python',
    long_description='''
wifi sniffer to expose iwlist wifi info or python
''',
    keywords='wifi iwlist python sniffer wifi wifi strength',
    author='Joel Tong',
    author_email='me@joeltong.org',
    url='https://github.com/easyNav/easyNav-sensors-wifi',
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: Unix',
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: Implementation :: PyPy",
        'Operating System :: OS Independent',
    ],
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        # add your dependencies here
        # remember to use 'package-name>=x.y.z,<x.y+1.0' notation (this way you get bugfixes)
    ],
    extras_require={
        'tests': tests_require,
    },
    entry_points={
        'console_scripts': [
            # add cli scripts here in this form:
            'easyNav-sensors-wifi=easyNav_sensors_wifi.cli:main',
        ],
    },
)

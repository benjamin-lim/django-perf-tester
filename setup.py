#!/usr/bin/env python
from setuptools import setup, find_packages

packages = find_packages()

setup(
    name='django-perf-project',
    version='0.0.1',
    description="",
    url='',
    packages=find_packages(),
    include_package_data=True,
    scripts=['manage.py', 'query.py', 'populate.py'],
)

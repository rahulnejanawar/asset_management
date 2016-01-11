# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
import os

version = '0.0.1'

setup(
    name='asset_management',
    version=version,
    description='App for managing IT/Fixed Assets',
    author='Rahul',
    author_email='rahulnejanawar@gmail.com',
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=("frappe",),
)

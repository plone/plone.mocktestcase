# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
import os

version = '1.0'

setup(
    name='plone.mocktestcase',
    version=version,
    description="Mock unit test case based on ``mocker``",
    long_description=(
        open("README.rst").read() + "\n" +
        open(os.path.join("CHANGES.rst")).read()
    ),
    # Get more strings from
    # http://www.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    keywords='',
    author='Martin Aspeli',
    author_email='optilude@gmail.com',
    url='http://plone.org',
    license='LGPL',
    packages=find_packages(exclude=['ez_setup']),
    namespace_packages=['plone'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'setuptools',
        'mocker',
        'zope.proxy',
        # 'zope.component',
        # -*- Extra requirements: -*-
    ],
    entry_points="""
    # -*- Entry points: -*-
    """,
)

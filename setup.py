from __future__ import print_function
from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand
import io
import codecs
import os
import sys
import sandman
import pytest

here = os.path.abspath(os.path.dirname(__file__))
LONG_DESCRIPTION = 'All Indian pilots are over here.'
with open('README.rst', 'r') as f:
   LONG_DESCRIPTION = f.read()
CLASSIFIERS = filter(None, map(str.strip,
"""
Development Status :: 0.0.1 - Development/Stable
Intended Audience :: Developers
License :: OSI Approved :: MIT License
License :: OSI Approved :: Academic Free License (AFL)
Programming Language :: Python
Programming Language :: Python :: 2
Programming Language :: Python :: 2.5
Programming Language :: Python :: 2.6
Programming Language :: Python :: 2.7
Programming Language :: Python :: Implementation :: CPython
Programming Language :: Python :: Implementation :: PyPy
Topic :: Software Development :: Libraries :: Python Modules
""".splitlines()))


def read(*filenames, **kwargs):
    encoding = kwargs.get('encoding', 'utf-8')
    sep = kwargs.get('sep', '\n')
    buf = []
    for filename in filenames:
        with io.open(filename, encoding=encoding) as f:
            buf.append(f.read())
    return sep.join(buf)


class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        errcode = pytest.main(self.test_args)
        sys.exit(errcode)

setup(
    name="pilote",
    version='0.0.1',
    description='',
    long_description=LONG_DESCRIPTION,
    classifiers=CLASSIFIERS,
    author="Om Prakash",
    author_email="omprakash@gofynd.com",
    url="https://github.com/omprakash1989/pilote/",
    license="MIT License",
    packages=['pilote', 'pilote.tests'],
    platforms=['any'],
    extras_require={
        'testing': ['pytest'],
    }
)

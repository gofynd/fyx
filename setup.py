from __future__ import print_function
from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand
import io
import os
import sys

here = os.path.abspath(os.path.dirname(__file__))
LONG_DESCRIPTION = 'All Indian pilots are over here.'
with open('README.md', 'r') as f:
   LONG_DESCRIPTION = f.read()
CLASSIFIERS = filter(None, map(str.strip,
"""
Development Status :: 2 - Pre-Alpha
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

EXCLUDES = ['contrib', 'docs', 'tests', 'htmlcov', 'docs', '.cache']


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
        import pytest
        errcode = pytest.main(self.test_args)
        sys.exit(errcode)

setup(
    name="fyx",
    include_package_data=True,
    version='0.0.9',
    description='',
    long_description=LONG_DESCRIPTION,
    classifiers=CLASSIFIERS,
    author="Fynd",
    author_email="omprakash@gofynd.com",
    url="https://github.com/gofynd/fyx/",
    license="MIT License",
    platforms=['any'],
    extras_require={
        'dev': ['check-manifest'],
        'test': ['coverage'],
    },
    # What does your project relate to?
    keywords='Integrate Delivery Partners like bluedart, delhivery, ecomm, fedex etc.',
    tests_require=['pytest'],
    setup_requires=['pytest-runner'],

    packages=find_packages(exclude=EXCLUDES),

    # If there are data files included in your packages that need to be
    # installed, specify them here.  If using Python 2.6 or less, then these
    # have to be included in MANIFEST.in as well.
    package_data={
        'pilote': ['pilote.dat'],
    },

    install_requires=['coverage', 'lxml', 'zeep', 'requests'],

    # Although 'package_data' is the preferred approach, in some case you may
    # need to place data files outside of your packages. See:
    # http://docs.python.org/3.4/distutils/setupscript.html#installing-additional-files # noqa
    # In this case, 'data_file' will be installed into '<sys.prefix>/my_data'
    data_files=[('pilote_data', ['data/data_file'])],

    # To provide executable scripts, use entry points in preference to the
    # "scripts" keyword. Entry points provide cross-platform support and allow
    # pip to create the appropriate form of executable for the target platform.
)

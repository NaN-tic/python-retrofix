#!/usr/bin/env python
# encoding: utf8
##############################################################################
#
#    Copyright (C) 2011-2013 NaN Projectes de Programari Lliure, S.L.
#                            http://www.NaN-tic.com
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################


from setuptools import setup, find_packages
import os

execfile(os.path.join('retrofix', 'version.py'))

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(name=PACKAGE,
    version=VERSION,
    description='retrofix',
    long_description=read('README'),
    author='NaN·tic',
    author_email='info@nan-tic.com',
    url=WEBSITE,
    download_url='https://pypi.python.org/pypi/retrofix/' + VERSION,
    packages=find_packages(),
    package_data={
        'retrofix.tests': ['c19.txt', 'c32.txt', 'c34.txt', 'c43.txt',
            'c58.txt'],
        },
    scripts=[],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: No Input/Output (Daemon)',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Libraries',
        ],
    license=LICENSE,
    install_requires=[
        'banknumber >= 1.0',
        ],
    extras_require={},
    zip_safe=False,
    test_suite='retrofix.tests',
    )

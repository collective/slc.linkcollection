# -*- coding: utf-8 -*-
"""
This module contains the slc.linkcollection package
"""
import os
from setuptools import setup, find_packages

def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

version = '1.3.5'

long_description = (
    read('README.txt')
    + '\n' +
    'Change history\n'
    '**************\n'
    + '\n' +
    read('CHANGES.txt')
    + '\n' +
    'Detailed Documentation\n'
    '**********************\n'
    + '\n' +
    read('slc', 'linkcollection', 'README.txt')
    + '\n' +
    'Contributors\n'
    '************\n'
    + '\n' +
    read('CONTRIBUTORS.txt')
    + '\n'
    )

tests_require=['zope.testing']


setup(name='slc.linkcollection',
      version=version,
      description="A viewlet displaying links to subdocuments and quickly loading their content via jquery",
      long_description=long_description,
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "License :: OSI Approved :: European Union Public Licence 1.1 (EUPL 1.1)",
        ],
      keywords='viewlet links jquery subnavigation',
      author='Syslab.com GmbH',
      author_email='info@syslab.com',
      url='http://svn.plone.org/svn/plone/plone.example',
      license='GPL + EUPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['slc'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
	  'plone.browserlayer',
	  
      ],
      tests_require=tests_require,
      extras_require=dict(tests=tests_require),
      test_suite = 'slc.linkcollection.tests.test_docs.test_suite',
      entry_points="""
      # -*- entry_points -*-
      """,
      )


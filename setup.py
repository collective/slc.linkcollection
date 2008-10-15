from setuptools import setup, find_packages
import os

version = '0.1'

setup(name='slc.linkcollection',
      version=version,
      description="A viewlet displaying links to subdocuments and quickly loading their content via kss",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='viewlet links kss subnaviation',
      author='Syslab.com GmbH',
      author_email='info@syslab.com',
      url='http://svn.plone.org/svn/plone/plone.example',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['slc'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
	  'plone.browserlayer',
	  
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )

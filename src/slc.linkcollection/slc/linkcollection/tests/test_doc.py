import os
import unittest

from zope.testing import doctest
from zope.component import testing
from Products.PloneTestCase import PloneTestCase
from Testing.ZopeTestCase import FunctionalDocFileSuite as Suite
from Products.PloneTestCase.layer import onsetup
from Globals import package_home
from slc.linkcollection import GLOBALS
from z3c.form import testing


class LinkCollectionFunctionalTestCase(PloneTestCase.FunctionalTestCase):
   pass

@onsetup
def setup_linkcollection():
    from Products.Five import zcml
    from Products.Five import fiveconfigure
    fiveconfigure.debug_mode = True
    import slc.linkcollection
    zcml.load_config('configure.zcml', slc.linkcollection)
    fiveconfigure.debug_mode = False

setup_linkcollection()

OPTIONFLAGS = (doctest.REPORT_ONLY_FIRST_FAILURE |
               doctest.ELLIPSIS |
               doctest.NORMALIZE_WHITESPACE)

PloneTestCase.setupPloneSite()



def test_suite():
    home = package_home(GLOBALS)
    print home+'/README.txt',
    return unittest.TestSuite([

        Suite(
           'README.txt',
           optionflags=OPTIONFLAGS,
           package='slc.linkcollection',
           setUp=testing.setUp, tearDown=testing.tearDown,
           test_class=LinkCollectionFunctionalTestCase
           ),
           
        ])

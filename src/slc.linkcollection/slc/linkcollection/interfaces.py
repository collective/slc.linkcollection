from zope.interface import Interface
from zope import schema
#from plone.app.z3cform.queryselect import ArchetypesContentSourceBinder

class ILinkCollectionLayer(Interface):
    """A layer specific to LinkCollection
    """
    
class ILinkList(Interface):
    urls = schema.TextLine(title=u"URL", readonly=False, required=False)

#    urls = schema.List(
#              title=u"URLS",
#              description=u"Search for urls",
#              value_type=schema.TextLine(title=(u"url"),)
#              )
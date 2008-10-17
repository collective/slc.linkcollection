from zope.interface import Interface
from zope import schema
from plone.app.vocabularies.catalog import SearchableTextSourceBinder
from Products.ATContentTypes.interface import IATDocument

class ILinkCollectionLayer(Interface):
    """A layer specific to LinkCollection
    """
    
class ILinkList(Interface):
    urls = schema.List(title=u"Referenced Documents",#
                       description=u"Find the document which provides the content",
                       required=True,
                       value_type=schema.Choice(title=u"Referenced Documents",
                                    description=u"Find the document which provides the content",
                                    source=SearchableTextSourceBinder({'object_provides' : IATDocument.__identifier__},
                                                                        default_query='path:'))
                       )


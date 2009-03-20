from Acquisition import aq_inner

from zope import schema
from zope.app.component.hooks import getSite
from zope.interface import Interface

from plone.app.vocabularies.catalog import SearchableTextSourceBinder, SearchableTextSource

from Products.ATContentTypes.interface import IATDocument
from Products.CMFCore.utils import getToolByName

class ILinkCollectionLayer(Interface):
    """A layer specific to LinkCollection
    """
    
class LocalSearchableTextSourceBinder(SearchableTextSourceBinder):
    """ make the binder search in the local folder first """

    def __call__(self, context):
        portal_url = getToolByName(context, 'portal_url', None)
        if IATDocument.implementedBy(context.__class__):
            parent = context.REQUEST.PARENTS[1]
        else:
            parent = getSite()
        current_path = '/'+'/'.join(portal_url.getRelativeContentPath(parent))
        self.default_query = 'path:%s' % current_path
        return SearchableTextSource(context, base_query=self.query.copy(),
                                    default_query=self.default_query)    
                                    
class ILinkList(Interface):
    urls = schema.List(
            title=u"Referenced Documents",
            description=\
u"""Search and select the documents you want to add to your linklist. The first box contains your current selection. Below it you can do a fulltext search for documents. Below the search are the search results you can pic from. Initially they show the contents of the current folder.""",
            required=True,
            value_type=schema.Choice(
                        title=u"Add documents for referencing",
                        source=LocalSearchableTextSourceBinder(
                                    {'object_provides':IATDocument.__identifier__}
                                )
                        )
            )
    

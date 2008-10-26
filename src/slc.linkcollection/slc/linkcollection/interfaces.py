from Acquisition import aq_inner
from zope.interface import Interface
from zope import schema
from plone.app.vocabularies.catalog import SearchableTextSourceBinder, SearchableTextSource
from Products.ATContentTypes.interface import IATDocument
from zope.app.component.hooks import getSite

class ILinkCollectionLayer(Interface):
    """A layer specific to LinkCollection
    """
    
class LocalSearchableTextSourceBinder(SearchableTextSourceBinder):
    """ make the binder search in the local folder first """

    def __call__(self, context):
        site = getSite()
        portal_url = site.portal_url
        current_path = '/'+'/'.join(portal_url.getRelativeContentPath(site.REQUEST.PARENTS[1]))
        self.default_query = 'path:%s' % current_path
        return SearchableTextSource(context, base_query=self.query.copy(),
                                    default_query=self.default_query)    
                                    
class ILinkList(Interface):
    urls = schema.List(title=u"Referenced Documents",
                       description=u"Search and select the documents you want to add to your linklist. The first box contains your current selection. Below it you can do a fulltext search for documents. Below the search are the search results you can pic from. Initially they show the contents of the current folder.",
                       required=True,
                       value_type=schema.Choice(title=u"Referenced Documents",
                                    description=u"!Search and select the documents you want to add to your linklist. The first box contains your current selection. Below it you can do a fulltext search for documents. Below the search are the search results you can pic from. Initially they show the contents of the current folder.",
                                    source=LocalSearchableTextSourceBinder({'object_provides' : IATDocument.__identifier__})
                                    )
                        )
    

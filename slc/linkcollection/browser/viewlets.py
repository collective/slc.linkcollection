from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone.app.layout.viewlets import common
from slc.linkcollection.interfaces import ILinkList
from types import *
from Products.CMFCore.utils import getToolByName
from zope.app.component.hooks import getSite
from Products.ATContentTypes.interface.document import IATDocument

class LinkBoxViewlet(common.ViewletBase):

    render = ViewPageTemplateFile('linkbox.pt')
    
    def show(self):
        user = getToolByName(self.context, 'portal_membership').getAuthenticatedMember()
        return user.has_permission('Modify portal content', self.context) or self.links()
        
    def raw(self):
        if not IATDocument.providedBy(self.context):
            return []
        urls = ILinkList(self.context).urls
        return urls
        
    def links(self):
        if not IATDocument.providedBy(self.context):
            return []
        urls = ILinkList(self.context).urls
        if not urls:
            return []
        portal = getSite()
        maps = []
        if type(urls) not in (ListType, TupleType):
            urls = [urls]
        for url in urls:
            if url.startswith('/'):
                url = url[1:]
            ob = portal.restrictedTraverse(url, None)
            
            if ob is not None:
                maps.append(dict(title=ob.Title(), url=url))
                
        return maps

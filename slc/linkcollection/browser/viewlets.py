from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone.app.layout.viewlets import common
from slc.linkcollection.interfaces import ILinkList
from types import *
from Products.CMFCore.utils import getToolByName
from zope.app.component.hooks import getSite
from Products.ATContentTypes.interface.document import IATDocument

class LinkBoxViewlet(common.ViewletBase):

    render = ViewPageTemplateFile('linkbox.pt')
    
    def showeditbox(self):
        user = getToolByName(self.context, 'portal_membership').getAuthenticatedMember()
        if user.has_permission('Modify portal content', self.context):
            return True
        return False
    
    def show(self):
        user = getToolByName(self.context, 'portal_membership').getAuthenticatedMember()
        if not IATDocument.providedBy(self.context):
            return False
        if user.has_permission('Modify portal content', self.context):
            return True
        if self.links() != []:
            return True
        return False
            
    def name_item(self, link):
        idx = self.links().index(link)
        return 'linklist-item-%s' % idx
        
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

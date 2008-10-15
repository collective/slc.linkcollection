from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone.app.layout.viewlets import common
from slc.linkcollection.interfaces import ILinkList
from types import *
from Products.CMFCore.utils import getToolByName

class LinkBoxViewlet(common.ViewletBase):

    render = ViewPageTemplateFile('linkbox.pt')
    
    def links(self):
        urls = ILinkList(self.context).urls
        portal = getToolByName(self.context, 'portal_url').getPortalObject()
        if not urls:
            return []
        maps = []
        if type(urls) not in (ListType, TupleType):
            urls = [urls]
        for url in urls:
            ob = portal.restrictedTraverse(url.encode('utf-8'), None)
            if ob is not None:
                maps.append(dict(title=ob.Title(), url=url))
                
        return maps

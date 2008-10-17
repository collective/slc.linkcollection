from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone.app.layout.viewlets import common
from slc.linkcollection.interfaces import ILinkList
from types import *
from Products.CMFCore.utils import getToolByName
from zope.app.component.hooks import getSite

class LinkBoxViewlet(common.ViewletBase):

    render = ViewPageTemplateFile('linkbox.pt')
    
    def links(self):
        urls = ILinkList(self.context).urls
        if not urls:
            return []
        portal = getSite()
        maps = []
        if type(urls) not in (ListType, TupleType):
            urls = [urls]
        for url in urls:
            ob = portal.restrictedTraverse(url[1:], None)
            
            if ob is not None:
                maps.append(dict(title=ob.Title(), url=url[1:]))
                
        return maps

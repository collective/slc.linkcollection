import Acquisition
from Products.Five.browser import BrowserView
from Products.CMFCore.utils import getToolByName
from kss.core.ttwapi import ( startKSSCommands, getKSSCommandSet, renderKSSCommands )
import logging
logger = logging.getLogger('slc.linkcollection')

class LinkCollectionLoad(BrowserView):
    """called by kss, loads body by given url
    """
    
    def __call__(self):
        url = self.request.get('url', None)
        startKSSCommands(self, self.request)
        logger.info(url)
        portal = getToolByName(self.context, 'portal_url').getPortalObject()
        item = portal.restrictedTraverse(url, None)
        if item is None:
            text = u'No document has been found at this URL: %s' % url
        else:
            title = unicode(item.Title(), 'utf-8')
            description = unicode(item.Description(), 'utf-8')
            bodytext = unicode(item.getText(), 'utf-8')
            text = """<h1 class="documentFirstHeading">%s</h1>
                      <div class="documentDescription">%s</div>
                      %s""" % (title, description, bodytext)
        core = getKSSCommandSet('core')
        core.replaceInnerHTML('#parent-fieldname-text', text)
        return renderKSSCommands()
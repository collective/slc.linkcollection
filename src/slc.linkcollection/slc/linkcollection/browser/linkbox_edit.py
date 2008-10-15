from zope import interface, schema, component
from z3c.form import form, field, button
from plone.app.z3cform.layout import wrap_form
from persistent import Persistent
from zope.annotation.interfaces import IAnnotations, IAttributeAnnotatable, IAnnotatable
from slc.linkcollection.interfaces import ILinkList
from Products.ATContentTypes.interface import IATDocument
from zope.annotation import factory

class LinkList(Persistent):
    interface.implements(ILinkList)
    component.adapts(IATDocument)
    urls = u""
    
linklist_adapter = factory(LinkList)

    
class LinkCollectionForm(form.Form):
    fields = field.Fields(ILinkList)
    label = u"Add Content Objects to point to"

    @button.buttonAndHandler(u'Apply')
    def handleApply(self, action):
        data, errors = self.extractData()
        ILinkList(self.context).urls = data['urls']



LinkCollectionView = wrap_form(LinkCollectionForm, label="Link Collection Form")
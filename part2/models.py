from mongoengine import EmbeddedDocument, Document
from mongoengine.fields import ListField, StringField, BooleanField, EmbeddedDocumentField


class Tag(EmbeddedDocument):
    name = StringField()

class Phone(EmbeddedDocument):
    number = StringField()

class Contact(Document):
    name = StringField(required=True)
    address = StringField()
    phones = ListField(EmbeddedDocumentField(Phone))
    email = StringField(required=True)
    sent = BooleanField(default=False)
    tags = ListField(EmbeddedDocumentField(Tag))


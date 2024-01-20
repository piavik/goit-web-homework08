# from datetime import datetime

from mongoengine import EmbeddedDocument, Document
from mongoengine.fields import ListField, StringField, ReferenceField#, EmbeddedDocumentField, DateTimeField


# class Tag(EmbeddedDocument):
#     name = StringField()

class Author(Document):
    fullname = StringField()
    born_date = StringField()
    born_location = StringField()
    description = StringField()


class Quotes(Document):
    tags = ListField() #EmbeddedDocumentField(Tag))
    author = ReferenceField('Author')
    quote = StringField()
    # meta = {'allow_inheritance': True}


from mongoengine import Document, StringField


class ParentCategory(Document):
    name = StringField()

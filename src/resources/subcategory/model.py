from mongoengine import Document, StringField


class Subcategory(Document):
    name = StringField()
    subcategory = StringField()

from mongoengine import Document, StringField


class category(Document):
    name = StringField()
    subcategory = StringField()

from mongoengine import Document, StringField


class user(Document):
    name = StringField()
    email = StringField()

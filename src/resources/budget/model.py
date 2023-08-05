from mongoengine import Document, StringField, DateTimeField


class budget(Document):
    name = StringField()
    date = DateTimeField()
    # TODO: Add userID
    # userID = StringField()
    sectionList = StringField()

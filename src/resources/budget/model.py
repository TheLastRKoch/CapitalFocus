from mongoengine import Document, StringField, DateTimeField


class budget(Document):
    name = StringField()
    date = DateTimeField()
    sectionList = StringField()
    userID = StringField()

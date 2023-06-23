from mongoengine import Document, StringField


class budget(Document):
    name = StringField()
    date = StringField()
    userID = StringField()
    sectionList = StringField()

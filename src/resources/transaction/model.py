from mongoengine import Document, StringField, IntField


class transaction(Document):
    name = StringField()
    date = StringField()
    userID = StringField()
    reference = StringField()
    amount = IntField()
    type = StringField()
    annotation = StringField()
    categotyID = StringField()

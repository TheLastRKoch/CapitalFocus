from mongoengine import Document, StringField, IntField


class unclassifiedTransaction(Document):
    name = StringField()
    date = StringField()
    userID = StringField()
    reference = StringField()
    amount = IntField()
    type = StringField()

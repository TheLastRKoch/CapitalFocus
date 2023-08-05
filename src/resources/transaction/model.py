from mongoengine import Document, StringField, IntField, DateField


class Transaction(Document):
    name = StringField()
    date = DateField()
    # userID = StringField()
    reference = StringField()
    amount = IntField()
    type = StringField()
    annotation = StringField()
    # categotyID = StringField()

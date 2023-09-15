from resources.unclassified_transaction.model import UnclassifiedTransaction
from database import session


class UnclassifiedTransactionRepository:

    def create(self, date, user, reference, description, amount, type):

        new = UnclassifiedTransaction(
            date=date,
            userID=user,
            reference=reference,
            description=description,
            amount=amount,
            type=type,
        )
        session.add(new)
        session.commit()
        return {"The unclassified transaction has been saved successfully", new}

    def get_list(self, userID):
        unclassified_transaction_list = session.query(UnclassifiedTransaction).filter(UnclassifiedTransaction.userID == userID)
        return [{
            "id": item.id,
            "date": item.date,
            "userID": item.userID,
            "reference": item.reference,
            "description": item.description,
            "amount": item.amount,
            "type": item.type
        } for item in unclassified_transaction_list]

    def get_by_id(self, id):
        unclassified_transaction_list = session.query(UnclassifiedTransaction).filter(UnclassifiedTransaction.id == id)
        return [{
            "id": item.id,
            "date": item.date,
            "userID": item.userID,
            "reference": item.reference,
            "description": item.description,
            "amount": item.amount,
            "type": item.type
        } for item in unclassified_transaction_list]

    def update_by_id(self, id, date,  reference, description, amount, type):

        unclassified_transaction = session.query(UnclassifiedTransaction).filter(UnclassifiedTransaction.id == id).first()

        unclassified_transaction.date = date
        unclassified_transaction.reference = reference
        unclassified_transaction.description = description
        unclassified_transaction.amount = amount
        unclassified_transaction.type = type
        session.commit()

        return unclassified_transaction

    def delete_by_id(self, id):
        unclassified_transaction = session.query(UnclassifiedTransaction).filter(UnclassifiedTransaction.id == id).first()
        session.delete(unclassified_transaction)
        return f"Element with the id {id} has been successfully removed"

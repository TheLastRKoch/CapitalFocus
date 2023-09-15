from resources.unclassified_transaction.repository import UnclassifiedTransactionRepository


class UnclassifiedTransactionService:

    def create(self, date, user, reference, description, amount, type):
        unclassified_transaction_new = UnclassifiedTransactionRepository()
        unclassified_transaction_new.create(date, user, reference, description, amount, type)
        return unclassified_transaction_new

    def get_list(self, userID):
        transaction_repository = UnclassifiedTransactionRepository()
        return transaction_repository.get_list(userID)

    def get_by_id(self, id):
        transaction_repository = UnclassifiedTransactionRepository()
        return transaction_repository.get_by_id(id)

    def delete(self, id):
        transaction_repository = UnclassifiedTransactionRepository()
        return transaction_repository.delete_by_id(id)

    def update(self, id, date, reference, description, amount, type):
        transaction_repository = UnclassifiedTransactionRepository()
        return transaction_repository.update_by_id(id, date, reference, description, amount, type)

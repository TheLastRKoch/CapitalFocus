from resources.unclassified_transaction.repository import UnclassifiedTransactionRepository


class UnclassifiedTransactionService:

    def create(self):
        transaction_repository = UnclassifiedTransactionRepository()
        return transaction_repository.get_by_id(0)

    def get_list(self):
        transaction_repository = UnclassifiedTransactionRepository()
        return transaction_repository.get_list()

    def get_by_id(self, id):
        transaction_repository = UnclassifiedTransactionRepository()
        return transaction_repository.get_by_id(id)

    def delete(self, id):
        transaction_repository = UnclassifiedTransactionRepository()
        return transaction_repository.delete_by_id(id)

    def update(self, id):
        transaction_repository = UnclassifiedTransactionRepository()
        return transaction_repository.update_by_id(id)

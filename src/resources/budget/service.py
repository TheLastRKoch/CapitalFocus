from resources.budget.repository import BudgetRepository


class BudgetService:

    def create(self):
        budget_repository = BudgetRepository()
        return budget_repository.get_by_id(0)

    def get_list(self):
        budget_repository = BudgetRepository()
        return budget_repository.get_list()

    def get_by_id(self, id):
        budget_repository = BudgetRepository()
        return budget_repository.get_by_id(id)

    def delete(self, id):
        budget_repository = BudgetRepository()
        return budget_repository.delete_by_id(id)

    def update(self, id):
        budget_repository = BudgetRepository()
        return budget_repository.update_by_id(id)

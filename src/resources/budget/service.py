from resources.budget.repository import BudgetRepository


class BudgetService:

    def create(self):
        pass

    def get_list(self):
        budget_repository = BudgetRepository()
        return budget_repository.get_list()

    def get_by_id(self, budget_id):
        budget_repository = BudgetRepository()
        return budget_repository.get_by_id(budget_id)

    def delete(self):
        pass

    def update(self):
        pass

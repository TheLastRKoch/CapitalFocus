from flask_restful import Resource

from resources.budget.service import BudgetService
from services.service_web import WebService


class BudgetController(Resource):
    url = "/budget"

    # List
    def get(self):
        # Services
        budget_service = BudgetService()
        web_service = WebService()

        body = budget_service.get_list()
        return web_service.response(200, body)

    # Create

    def post(self):
        pass


class BudgetIDController(Resource):
    url = "/budget/<budget_id>"

    # Get by ID
    def get(self, budget_id):
        # Services
        budget_service = BudgetService()
        web_service = WebService()

        body = budget_service.get_by_id(budget_id)
        return web_service.response(200, body)

    # Update by ID
    def put(self, budget_id):
        pass

    def delete(self, budget_id):
        pass


def add_budget_resource_table(api):
    api.add_resource(BudgetController, BudgetController.url)
    api.add_resource(BudgetIDController, BudgetIDController.url)

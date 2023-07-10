from resources.transaction.service import TransactionService
from services.service_web import WebService
from flask_restful import Resource


class TransactionController(Resource):
    url = "/transaction"

    # List
    def get(self):
        # Services
        transaction_service = TransactionService()
        web_service = WebService()
        body = transaction_service.get_list()
        return web_service.response(200, body)

    # Create

    def post(self):
        pass


class TransactionIDController(Resource):
    url = "/transaction/<id>"

    # Get by ID
    def get(self, id):
        # Services
        transaction_service = TransactionService()
        web_service = WebService()

        body = transaction_service.get_by_id(id)
        return web_service.response(200, body)

    # Update by ID
    def put(self, id):
        # Services
        transaction_service = TransactionService()
        web_service = WebService()

        body = transaction_service.get_by_id(id)
        return web_service.response(200, body)

    def delete(self, id):
        # Services
        transaction_service = TransactionService()
        web_service = WebService()

        body = transaction_service.get_by_id(id)
        return web_service.response(200, body)


def add_transaction_resource_table(api):
    api.add_resource(TransactionController, TransactionController.url)
    api.add_resource(TransactionIDController, TransactionIDController.url)

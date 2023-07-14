from resources.unclassified_transaction.service import UnclassifiedTransactionService
from services.service_web import WebService
from flask_restful import Resource


class UnclassifiedTransactionController(Resource):
    url = "/unclassified_transaction"

    # List
    def get(self):
        # Services
        unclassified_transaction_service = UnclassifiedTransactionService()
        web_service = WebService()
        
        body = unclassified_transaction_service.get_list()
        return web_service.response(200, body)

    # Create

    def post(self):
        pass


class UnclassifiedTransactionIDController(Resource):
    url = "/unclassified_transaction/<id>"

    # Get by ID
    def get(self, id):
        # Services
        unclassified_transaction_service = UnclassifiedTransactionService()
        web_service = WebService()

        body = unclassified_transaction_service.get_by_id(id)
        return web_service.response(200, body)

    # Update by ID
    def put(self, id):
        # Services
        UnclassifiedTransaction_service = UnclassifiedTransactionService()
        web_service = WebService()

        body = UnclassifiedTransaction_service.get_by_id(id)
        return web_service.response(200, body)

    def delete(self, id):
        # Services
        UnclassifiedTransaction_service = UnclassifiedTransactionService()
        web_service = WebService()

        body = UnclassifiedTransaction_service.get_by_id(id)
        return web_service.response(200, body)


def add_unclassified_transaction_resource_table(api):
    api.add_resource(UnclassifiedTransactionController,
                     UnclassifiedTransactionController.url)

    api.add_resource(UnclassifiedTransactionIDController,
                     UnclassifiedTransactionIDController.url)

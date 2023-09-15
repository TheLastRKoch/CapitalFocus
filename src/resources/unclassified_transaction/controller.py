from resources.unclassified_transaction.service import UnclassifiedTransactionService
from services.service_auth import check_token
from services.service_web import WebService
from flask_restful import Resource
from flask import request


class UnclassifiedTransactionController(Resource):
    url = "/unclassified_transaction"

    @check_token
    def post(self):

        # Service definition
        unclassified_transaction_service = UnclassifiedTransactionService()

        userID = request.user["users"][0]["localId"]
        body = request.json

        unclassified_transaction_service.create(
            body["date"],
            userID,
            body["reference"],
            body["description"],
            body["amount"],
            body["type"],
        )

    # List
    @check_token
    def get(self):
        # Services
        unclassified_transaction_service = UnclassifiedTransactionService()
        web_service = WebService()

        userID = request.user["users"][0]["localId"]

        body = unclassified_transaction_service.get_list(userID)
        return web_service.response(200, body)


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

        # Service definition
        unclassified_transaction_service = UnclassifiedTransactionService()

        body = request.json

        unclassified_transaction_service.update(
            id,
            body["date"],
            body["reference"],
            body["description"],
            body["amount"],
            body["type"],
        )

    def delete(self, id):
        # Services
        UnclassifiedTransaction_service = UnclassifiedTransactionService()
        web_service = WebService()

        body = UnclassifiedTransaction_service.delete(id)
        return web_service.response(200, body)


class UnclassifiedTransactionIDClassifyController(Resource):

    url = "/unclassified_transaction/<id>/classify"

    def put(self, id):
        return {"msg": "This feature stills in process"}


def add_unclassified_transaction_resource_table(api):
    api.add_resource(UnclassifiedTransactionController,
                     UnclassifiedTransactionController.url)

    api.add_resource(UnclassifiedTransactionIDController,
                     UnclassifiedTransactionIDController.url)

    api.add_resource(UnclassifiedTransactionIDClassifyController,
                     UnclassifiedTransactionIDClassifyController.url)

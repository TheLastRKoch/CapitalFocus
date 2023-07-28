from flask_restful import Resource


class StatusController(Resource):
    url = "/status"

    def get(self):
        return {"msg": "Status OK"}


class StatusHomeController(Resource):
    url = "/"

    def get(self):
        return {"paths": [
            "http://127.0.0.1:5000/status",
            "http://127.0.0.1:5000/category",
            "http://127.0.0.1:5000/budget",
            "http://127.0.0.1:5000/transaction",
            "http://127.0.0.1:5000/unclassified_transaction"
        ]}


def add_status_resource_table(api):
    api.add_resource(StatusController, StatusController.url)
    api.add_resource(StatusHomeController, StatusHomeController.url)

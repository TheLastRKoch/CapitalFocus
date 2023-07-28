from resources.user.service import UserService
from services.service_web import WebService
from flask_restful import Resource


class UserController(Resource):
    url = "/user"

    # List
    def get(self):
        # Services
        user_service = UserService()
        web_service = WebService()
        body = user_service.get_list()
        return web_service.response(200, body)

    # Create

    def post(self):
        pass


class UserIDController(Resource):
    url = "/user/<id>"

    # Get by ID
    def get(self, id):
        # Services
        user_service = UserService()
        web_service = WebService()

        body = user_service.get_by_id(id)
        return web_service.response(200, body)

    # Update by ID
    def put(self, id):
        # Services
        user_service = UserService()
        web_service = WebService()

        body = user_service.get_by_id(id)
        return web_service.response(200, body)

    def delete(self, id):
        # Services
        user_service = UserService()
        web_service = WebService()

        body = user_service.get_by_id(id)
        return web_service.response(200, body)


def add_user_resource_table(api):
    api.add_resource(UserController, UserController.url)
    api.add_resource(UserIDController, UserIDController.url)

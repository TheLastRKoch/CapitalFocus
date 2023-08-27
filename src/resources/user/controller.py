from services.service_auth import login
from flask_restful import Resource
from flask import request


class UserController(Resource):
    url = "/user/login"

    def post(self):

        body = request.json
        user = login(body["email"], body["password"])
        if user is None:
            return {"message": "Email or password is not valid"}, 400
        return {"message": "User authenticated successfully", "userToken": user}, 200


def add_user_resource_table(api):
    api.add_resource(UserController, UserController.url)

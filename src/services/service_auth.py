from firebase_admin import auth
from flask import request


def check_token(func):
    def wrapper(*args, **kwargs):
        if not request.headers.get("authorization"):
            return {"message": "No auth token provided"}, 400
        try:
            user = auth.verify_id_token(request.headers["authorization"])
            request.user = user
        except Exception as ex:
            print(ex)
            return {"message": "Invalid token provided"}, 400
        # TODO: Add loggin
        return func(*args, **kwargs)
    return wrapper

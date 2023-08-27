from os import environ as env
from flask import request
import pyrebase


def check_token(func):
    def wrapper(*args, **kwargs):
        config = {
            "apiKey": env["API_KEY"],
            "authDomain": env["AUTH_DOMAIN"],
            "projectId":  env["PROJECT_ID"],
            "storageBucket":  env["STORAGE_BUCKET"],
            "messagingSenderId":  env["MESSAGING_SENDER_ID"],
            "appId":  env["APP_ID"],
            "measurementId":  env["MEASUREMENT_ID"],
            "databaseURL": ""
        }
        firebase = pyrebase.initialize_app(config)

        if not request.headers.get("Authorization"):
            return {"message": "No auth token provided"}, 400
        try:
            auth = firebase.auth()
            token = request.headers.get("Authorization").replace("bearer ", "")
            user = auth.get_account_info(token)
            request.user = user
        except Exception as ex:
            print(ex)
            return {"message": "Invalid token provided"}, 400
        # TODO: Add loggin
        return func(*args, **kwargs)
    return wrapper


def login(email, password):
    config = {
        "apiKey": env["API_KEY"],
        "authDomain": env["AUTH_DOMAIN"],
        "projectId":  env["PROJECT_ID"],
        "storageBucket":  env["STORAGE_BUCKET"],
        "messagingSenderId":  env["MESSAGING_SENDER_ID"],
        "appId":  env["APP_ID"],
        "measurementId":  env["MEASUREMENT_ID"],
        "databaseURL": ""
    }
    firebase = pyrebase.initialize_app(config)

    try:
        auth = firebase.auth()
        return auth.sign_in_with_email_and_password(email, password)["idToken"]
    except Exception as ex:
        print(ex)
        return None
    # TODO: Add loggin

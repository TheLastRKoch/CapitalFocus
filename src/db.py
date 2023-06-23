from pymongo.mongo_client import MongoClient
from os import environ as env


class db:
    def __init__(self):
        client = MongoClient(env["uri"])
        try:
            client.admin.command("ping")
            return client
        except Exception as err:
            # TODO: Add login
            print("Error: "+err)

from resources.unclassified_transaction.controller import add_unclassified_transaction_resource_table
from resources.category.controller import add_category_resource_table
from resources.transaction.controller import add_transaction_resource_table
from resources.budget.controller import add_budget_resource_table
from resources.status.controller import add_status_resource_table
from mongoengine import connect
from dotenv import load_dotenv
from os import environ as env
from flask_restful import Api
from flask import Flask


# Load .env file
load_dotenv()


# Load .env file
load_dotenv()


# Connect to MongoDB
connect(host=env["uri"])


# Init App
app = Flask(__name__)
api = Api(app)


# Endpoint table routes
add_unclassified_transaction_resource_table(api)
add_transaction_resource_table(api)
add_category_resource_table(api)
add_status_resource_table(api)
add_budget_resource_table(api)


# Main
if __name__ == "__main__":
    app.run()

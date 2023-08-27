from resources.unclassified_transaction.controller import add_unclassified_transaction_resource_table
from resources.parent_category.controller import add_parent_category_resource_table
from resources.subcategory.controller import add_subcategory_resource_table
from resources.transaction.controller import add_transaction_resource_table
from resources.budget.controller import add_budget_resource_table
from resources.status.controller import add_status_resource_table
from resources.user.controller import add_user_resource_table
from mongoengine import connect
from dotenv import load_dotenv
from flask_restful import Api
from os import environ as env
from flask import Flask


# Load .env file
load_dotenv()


# Init App
app = Flask(__name__)
api = Api(app)

# DB
connect(host=env["MONGO_URI"])

# Endpoint table routes
add_unclassified_transaction_resource_table(api)
add_parent_category_resource_table(api)
add_transaction_resource_table(api)
add_subcategory_resource_table(api)
add_status_resource_table(api)
add_budget_resource_table(api)
add_user_resource_table(api)


# Main
if __name__ == "__main__":
    app.run(debug=True)

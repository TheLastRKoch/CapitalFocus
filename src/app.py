from resources.unclassified_transaction.controller import add_unclassified_transaction_resource_table
from resources.subcategory.controller import add_subcategory_resource_table
from resources.transaction.controller import add_transaction_resource_table
from resources.category.controller import add_category_resource_table
from resources.budget.controller import add_budget_resource_table
from resources.status.controller import add_status_resource_table
from resources.user.controller import add_user_resource_table
from dotenv import load_dotenv
from flask_restful import Api
from flask import Flask

# Load .env file
load_dotenv()


# Init App
app = Flask(__name__)
api = Api(app)

# Endpoint table routes
add_unclassified_transaction_resource_table(api)
add_category_resource_table(api)
add_transaction_resource_table(api)
add_subcategory_resource_table(api)
add_status_resource_table(api)
add_budget_resource_table(api)
add_user_resource_table(api)


# Main
if __name__ == "__main__":
    app.run(debug=True)

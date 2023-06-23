from resources.status.controller import add_status_resource_table
from dotenv import load_dotenv
from flask_restful import Api
from flask import Flask


# Load .env file
load_dotenv()

# Init App
app = Flask(__name__)
api = Api(app)


# Endpoint table routes
add_status_resource_table(api)


if __name__ == "__main__":
    app.run()

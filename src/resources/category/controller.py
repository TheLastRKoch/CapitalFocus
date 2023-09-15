from resources.category.service import CategoryService
from services.service_web import WebService
from flask_restful import Resource


class CategoryController(Resource):
    url = "/category"

    # List
    def get(self):
        # Services
        parent_category_service = CategoryService()
        web_service = WebService()
        body = parent_category_service.get_list()
        return web_service.response(200, body)

    # Create

    def post(self):
        pass


class CategoryIDController(Resource):
    url = "/category/<id>"

    # Get by ID
    def get(self, id):
        # Services
        parent_category_service = CategoryService()
        web_service = WebService()

        body = parent_category_service.get_by_id(id)
        return web_service.response(200, body)

    # Update by ID
    def put(self, id):
        # Services
        parent_category_service = CategoryService()
        web_service = WebService()

        body = parent_category_service.get_by_id(id)
        return web_service.response(200, body)

    def delete(self, id):
        # Services
        parent_category_service = CategoryService()
        web_service = WebService()

        body = parent_category_service.get_by_id(id)
        return web_service.response(200, body)


def add_category_resource_table(api):
    api.add_resource(CategoryController, CategoryController.url)
    api.add_resource(CategoryIDController, CategoryIDController.url)

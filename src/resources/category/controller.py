from resources.parent_category.service import CategoryService
from services.service_web import WebService
from flask_restful import Resource


class ParentCategoryController(Resource):
    url = "/category"

    # List
    def get(self):
        # Services
        parent_category_service = ParentCategoryService()
        web_service = WebService()
        body = parent_category_service.get_list()
        return web_service.response(200, body)

    # Create

    def post(self):
        pass


class ParentCategoryIDController(Resource):
    url = "/category/<id>"

    # Get by ID
    def get(self, id):
        # Services
        parent_category_service = ParentCategoryService()
        web_service = WebService()

        body = parent_category_service.get_by_id(id)
        return web_service.response(200, body)

    # Update by ID
    def put(self, id):
        # Services
        parent_category_service = ParentCategoryService()
        web_service = WebService()

        body = parent_category_service.get_by_id(id)
        return web_service.response(200, body)

    def delete(self, id):
        # Services
        parent_category_service = ParentCategoryService()
        web_service = WebService()

        body = parent_category_service.get_by_id(id)
        return web_service.response(200, body)


def add_parent_category_resource_table(api):
    api.add_resource(ParentCategoryController, ParentCategoryController.url)
    api.add_resource(ParentCategoryIDController, ParentCategoryIDController.url)

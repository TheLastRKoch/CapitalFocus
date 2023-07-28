from resources.subcategory.service import SubcategoryService
from services.service_web import WebService
from flask_restful import Resource


class SubcategoryController(Resource):
    url = "/subcategory"

    # List
    def get(self):
        # Services
        subcategory_service = SubcategoryService()
        web_service = WebService()
        body = subcategory_service.get_list()
        return web_service.response(200, body)

    # Create

    def post(self):
        pass


class SubcategoryIDController(Resource):
    url = "/subcategory/<id>"

    # Get by ID
    def get(self, id):
        # Services
        subcategory_service = SubcategoryService()
        web_service = WebService()

        body = subcategory_service.get_by_id(id)
        return web_service.response(200, body)

    # Update by ID
    def put(self, id):
        # Services
        subcategory_service = SubcategoryService()
        web_service = WebService()

        body = subcategory_service.get_by_id(id)
        return web_service.response(200, body)

    def delete(self, id):
        # Services
        subcategory_service = SubcategoryService()
        web_service = WebService()

        body = subcategory_service.get_by_id(id)
        return web_service.response(200, body)


def add_subcategory_resource_table(api):
    api.add_resource(SubcategoryController, SubcategoryController.url)
    api.add_resource(SubcategoryIDController, SubcategoryIDController.url)

from services.service_file import FileService
import json


class BudgetRepository:

    # ! Mock
    def get_list(self):
        service_file = FileService()
        return json.loads(service_file.read_textfile("examples/budget-response.jsonc"))

    # ! Mock
    def get_by_id(self, budget_id):
        service_file = FileService()
        return json.loads(service_file.read_textfile(
            "examples/budget-response.jsonc"))["items"][0]

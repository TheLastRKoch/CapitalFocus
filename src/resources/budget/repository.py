from services.service_file import FileService
import json


class BudgetRepository:

    def __init__(self):
        pass

    # !Mock
    def get_list(self):

        view = list(self.collection.find({}))
        return view

    # !Mock
    def get_by_id(self, id):
        service_file = FileService()
        return json.loads(service_file.read_textfile(
            "examples/budget/list.jsonc"))["items"][int(id)]

    # !Mock
    def update_by_id(self, id):
        return self.get_by_id(id)

    # !Mock
    def delete_by_id(self, id):
        return True

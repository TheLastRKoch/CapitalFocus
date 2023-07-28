from services.service_file import FileService
import json


class SubcategoryRepository:

    # !Mock
    def get_list(self):
        service_file = FileService()
        return json.loads(service_file.read_textfile(
            "examples/subcategory/list.jsonc"
        ))

    # !Mock
    def get_by_id(self, id):
        service_file = FileService()
        return json.loads(service_file.read_textfile(
            "examples/subcategory/list.jsonc"))["items"][int(id)]

    # !Mock
    def update_by_id(self, id):
        return self.get_by_id(id)

    # !Mock
    def delete_by_id(self, id):
        return True

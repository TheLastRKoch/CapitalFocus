from services.service_file import FileService
import json


class TransactionRepository:

    # !Mock
    def get_list(self):
        service_file = FileService()
        return json.loads(service_file.read_textfile(
            "examples/transaction/list.jsonc"
        ))

    # !Mock
    def get_by_id(self, id):
        service_file = FileService()
        return json.loads(service_file.read_textfile(
            "examples/transaction/list.jsonc"))["items"][int(id)]

    # !Mock
    def update_by_id(self, id):
        return self.get_by_id(id)

    # !Mock
    def delete_by_id(self, id):
        return True

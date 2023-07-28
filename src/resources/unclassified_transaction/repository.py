from services.service_file import FileService
import jmespath
import json


class UnclassifiedTransactionRepository:

    # !Mock
    def get_list(self):
        service_file = FileService()
        return json.loads(service_file.read_textfile(
            "examples/unclassified_transaction/list.jsonc"
        ))

    # !Mock
    def get_by_id(self, id):
        service_file = FileService()
        return jmespath.search(f"@.items[?contains (id, '{id}')] | [0]", json.loads(service_file.read_textfile(
            "examples/unclassified_transaction/list.jsonc")))

    # !Mock
    def update_by_id(self, id):
        return self.get_by_id(id)

    # !Mock
    def delete_by_id(self, id):
        return True

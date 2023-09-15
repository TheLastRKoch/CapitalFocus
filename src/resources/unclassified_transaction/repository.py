from resources.unclassified_transaction.model import UnclassifiedTransaction
from services.service_file import FileService
from database import session
import jmespath
import json


class UnclassifiedTransactionRepository:

    def create(self, date, user, reference, description, amount, type):

        new = UnclassifiedTransaction(
            date=date,
            userID=user,
            reference=reference,
            description=description,
            amount=amount,
            type=type,
        )
        session.add(new)
        session.commit()
        return {"The unclassified transaction has been saved successfully", new}

    # !Mock

    def get_list(self):
        view = session.query(UnclassifiedTransaction)
        return None

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

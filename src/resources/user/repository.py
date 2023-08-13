import json
from resources.user.model import User


class UserRepository:

    def create(self, name, email):
        new = User(name=name, email=email)
        new.save()

    def get_by_id(self, id):
        return json.loads(User.objects.get(id=id).to_json())

    # !Mock
    def update_by_id(self, id, name, email):
        user_to_update = json.loads(User.objects.get(id=id).to_json())
        user_to_update.name = name
        user_to_update.email = email
        user_to_update.save()


    # !Mock
    def delete_by_id(self, id):
        return True

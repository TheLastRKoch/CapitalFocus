from resources.user.repository import UserRepository


class UserService:

    def create(self):
        user_repository = UserRepository()
        return user_repository.get_by_id(0)

    def get_by_id(self, id):
        user_repository = UserRepository()
        return user_repository.get_by_id(id)

    def delete(self, id):
        user_repository = UserRepository()
        return user_repository.delete_by_id(id)

    def update(self, id, name, email):
        user_repository = UserRepository()
        return user_repository.update_by_id(id, name, email)

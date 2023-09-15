from resources.category.repository import CategoryRepository


class CategoryService:

    def create(self):
        parent_category_repository = CategoryRepository()
        return parent_category_repository.get_by_id(0)

    def get_list(self):
        parent_category_repository = CategoryRepository()
        return parent_category_repository.get_list()

    def get_by_id(self, id):
        parent_category_repository = CategoryRepository()
        return parent_category_repository.get_by_id(id)

    def delete(self, id):
        parent_category_repository = CategoryRepository()
        return parent_category_repository.delete_by_id(id)

    def update(self, id):
        parent_category_repository = CategoryRepository()
        return parent_category_repository.update_by_id(id)

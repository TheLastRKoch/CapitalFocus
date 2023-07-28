from resources.subcategory.repository import SubcategoryRepository


class SubcategoryService:

    def create(self):
        category_repository = SubcategoryRepository()
        return category_repository.get_by_id(0)

    def get_list(self):
        category_repository = SubcategoryRepository()
        return category_repository.get_list()

    def get_by_id(self, id):
        category_repository = SubcategoryRepository()
        return category_repository.get_by_id(id)

    def delete(self, id):
        category_repository = SubcategoryRepository()
        return category_repository.delete_by_id(id)

    def update(self, id):
        category_repository = SubcategoryRepository()
        return category_repository.update_by_id(id)

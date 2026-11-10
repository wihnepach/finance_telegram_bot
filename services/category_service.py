from models.category import Category
from repositories.category_repository import category_repository


class CategoryService:

    async def create_category(
        self,
        user_id: int,
        name: str,
        category_type: str,
        emoji: str = "📁"
    ):
        category = Category(
            user_id=user_id,
            name=name,
            type=category_type,
            emoji=emoji
        )

        return await category_repository.create(category)

    async def get_user_categories(self, user_id: int):
        return await category_repository.get_by_user(user_id)

    async def get_income_categories(self, user_id: int):
        return await category_repository.get_by_type(
            user_id, "income"
        )

    async def get_expense_categories(self, user_id: int):
        return await category_repository.get_by_type(
            user_id, "expense"
        )

    async def delete_category(self, user_id: int, category_id: str):
        return await category_repository.delete(user_id, category_id)


category_service = CategoryService()
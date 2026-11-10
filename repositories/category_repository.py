from database.connection import database
from models.category import Category


class CategoryRepository:

    def __init__(self):
        self.collection = database.db["categories"]

    async def create(self, category: Category):
        category_data = category.model_dump()

        result = await self.collection.insert_one(category_data)

        return str(result.inserted_id)

    async def get_by_user(self, user_id: int):
        cursor = self.collection.find({"user_id": user_id})

        categories = []

        async for category in cursor:
            category.pop("_id", None)
            categories.append(Category(**category))

        return categories

    async def get_by_type(self, user_id: int, category_type: str):
        cursor = self.collection.find({
            "user_id": user_id,
            "type": category_type
        })

        categories = []

        async for category in cursor:
            category.pop("_id", None)
            categories.append(Category(**category))

        return categories

    async def delete(self, user_id: int, category_id: str):
        from bson import ObjectId

        result = await self.collection.delete_one({
            "_id": ObjectId(category_id),
            "user_id": user_id
        })

        return result.deleted_count > 0


category_repository = CategoryRepository()
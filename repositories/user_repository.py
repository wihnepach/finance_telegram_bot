from models.user import User
from database.connection import database


class UserRepository:

    def __init__(self):
        self.collection = database.db["users"]

    async def get_by_telegram_id(self, telegram_id: int):
        user_data = await self.collection.find_one(
            {"telegram_id": telegram_id}
        )

        if user_data:
            return User(**user_data)

        return None

    async def create(self, user: User):
        user_data = user.model_dump()

        await self.collection.insert_one(user_data)

        return user

    async def get_or_create(
        self,
        telegram_id: int,
        username: str | None,
        first_name: str
    ):
        user = await self.get_by_telegram_id(telegram_id)

        if user:
            return user

        new_user = User(
            telegram_id=telegram_id,
            username=username,
            first_name=first_name
        )

        await self.create(new_user)

        return new_user

    async def update(self, telegram_id: int, update_data: dict):
        result = await self.collection.update_one(
            {"telegram_id": telegram_id},
            {"$set": update_data}
        )

        return result.modified_count > 0


user_repository = UserRepository()
from motor.motor_asyncio import AsyncIOMotorClient
from config import settings


class Database:
    def __init__(self):
        self.client = AsyncIOMotorClient(settings.MONGODB_URL)
        self.db = self.client[settings.DATABASE_NAME]

    async def connect(self):
        await self.client.admin.command("ping")
        print("Успешное подключение к MongoDB!")

    async def close(self):
        self.client.close()


database = Database()
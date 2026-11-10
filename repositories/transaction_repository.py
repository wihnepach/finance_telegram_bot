from database.connection import database
from models.transaction import Transaction


class TransactionRepository:

    def __init__(self):
        self.collection = database.db["transactions"]

    async def create(self, transaction: Transaction):
        transaction_data = transaction.model_dump()

        result = await self.collection.insert_one(transaction_data)

        return str(result.inserted_id)

    async def get_by_user(self, user_id: int, limit: int = 20):
        cursor = (
            self.collection
            .find({"user_id": user_id})
            .sort("occurred_at", -1)
            .limit(limit)
        )

        transactions = []

        async for transaction in cursor:
            transaction.pop("_id", None)
            transactions.append(Transaction(**transaction))

        return transactions

    async def get_total_by_type(self, user_id: int, transaction_type: str):
        result = await self.collection.aggregate([
            {
                "$match": {
                    "user_id": user_id,
                    "type": transaction_type
                }
            },
            {
                "$group": {
                    "_id": None,
                    "total": {"$sum": "$amount"}
                }
            }
        ]).to_list(length=1)

        if result:
            return result[0]["total"]

        return 0

    async def get_balance(self, user_id: int):
        income = await self.get_total_by_type(user_id, "income")
        expense = await self.get_total_by_type(user_id, "expense")

        return income - expense


transaction_repository = TransactionRepository()
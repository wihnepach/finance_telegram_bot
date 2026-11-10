from models.transaction import Transaction
from repositories.transaction_repository import transaction_repository


class TransactionService:

    async def add_transaction(
        self,
        user_id: int,
        category_id: str,
        transaction_type: str,
        amount: int,
        description: str | None = None
    ):
        transaction = Transaction(
            user_id=user_id,
            category_id=category_id,
            type=transaction_type,
            amount=amount,
            description=description
        )

        return await transaction_repository.create(transaction)

    async def get_history(self, user_id: int, limit: int = 20):
        return await transaction_repository.get_by_user(user_id, limit)

    async def get_income(self, user_id: int):
        return await transaction_repository.get_total_by_type(
            user_id, "income"
        )

    async def get_expenses(self, user_id: int):
        return await transaction_repository.get_total_by_type(
            user_id, "expense"
        )

    async def get_balance(self, user_id: int):
        return await transaction_repository.get_balance(user_id)


transaction_service = TransactionService()
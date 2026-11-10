import asyncio
from database.connection import database


async def main():
    try:
        await database.connect()
    except Exception as error:
        print(f"Ошибка подключения: {error}")
    finally:
        await database.close()


if __name__ == "__main__":
    asyncio.run(main())
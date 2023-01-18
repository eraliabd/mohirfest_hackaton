import asyncio

from utils.db_api.postgresql import Database


async def test():
    db = Database()
    await db.create()

    print("receiver jadvalini yaratamiz...")
    # await db.drop_users()
    # await db.create_table_users()
    print("Yaratildi")

    print("Foydalanuvchilarni qo'shamiz")

    await db.add_user("erali", 22, "+998907896543", "Guliston", "dasturchi", "zo'r bo'lish")
    await db.add_user("sherali", 20, "+998907896543", "Guliston", "dasturchi", "aqilli bo'lish")
    print("Qo'shildi")

    users = await db.select_all_users()
    print(f"Barcha foydalanuvchilar: {users}")

    user = await db.select_user(id=1)
    print(f"Foydalanuvchi: {user}")


asyncio.run(test())

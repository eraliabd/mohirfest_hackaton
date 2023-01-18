import asyncio

from aiogram import types
from aiogram.dispatcher.filters import Command

from data.config import ADMINS
from loader import dp, db, bot


# @dp.message_handler(text="/reklama", user_id=ADMINS)
# async def send_ad_to_all(message: types.Message):
#     users = await db.select_all_users()
#     for user in users:
#         # print(user[3])
#         user_id = user[3]
#         await bot.send_message(chat_id=user_id, text="@python_backend_dev kanalimizga obuna bo'ling!")
#         await asyncio.sleep(0.05)
#
#
# @dp.message_handler(Command('users_count'))
# async def users_counter(message: types.Message):
#     users = await db.count_users()
#     print("soni: ", users)
#     await bot.send_message(chat_id=ADMINS[0], text=f"Botdagi foydalanuvchilar soni {users} ta yetgan")
#     await message.answer("Sizga foydalanuvchilar sonini ko'rish huquqi berilmagan!")


# with open('D:\\Backend\\Aiogram\\main_lessons\\downloads\\charities\\photos\\file_25.jpg', 'rb') as f:
#     file = f.read()
#     print(file)
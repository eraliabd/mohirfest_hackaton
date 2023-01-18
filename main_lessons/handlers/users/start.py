import asyncpg
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from keyboards.default.menuKeyboard import menu
from keyboards.default.startKeyboard import contact_button, location_button
from . anketa import enter_test
from loader import dp, db, bot
from data.config import ADMINS
from .menu import show_menu


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    user = message.from_user.full_name
    # try:
    #     user = await db.add_user(telegram_id=message.from_user.id,
    #                              full_name=message.from_user.full_name,
    #                              username=message.from_user.username)
    # except asyncpg.exceptions.UniqueViolationError:
    #     user = await db.select_user(telegram_id=message.from_user.id)

    await message.answer(f"Assalomu alaykum {user}, Ulashing botimizga xush kelibsiz!\n\n"
                         f"O'zingizga kerakli kategoriyani tanlang 👇🏻", reply_markup=menu)
    # await show_menu(message=message)

    # ADMINGA xabar beramiz
    # count = await db.count_users()
    # msg = f"{user[1]} bazaga qo'shildi.\nBazada {count} ta foydalanuvchi bor."
    # await bot.send_message(chat_id=ADMINS[0], text=msg)

from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, ReplyKeyboardRemove

from handlers.users.anketa import enter_test
from handlers.users.rentUser import enter_rent
from keyboards.default.menuKeyboard import menu

from loader import dp


@dp.message_handler(Command("menu"))
async def show_menu(message: Message):
    await message.answer("E'lon joylash uchun o'zingizga mos kategoriyani tanlang")


@dp.message_handler(text='Oluvchi')
async def send_link(message: Message):
    await enter_test(message=message)


@dp.message_handler(text='Xayriya')
async def send_charity(message: Message):
    await enter_rent(message=message)

from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp
from states.personalData import ReceiverData
from loader import dp


@dp.message_handler(CommandHelp(), state=ReceiverData.full_name)
async def bot_help(message: types.Message):
    text = ("Ism va familiyangizni kiriting, iltimos")

    await message.answer(text)


@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    text = ("Buyruqlar: ",
            "/start - Botni ishga tushirish",
            "/help - Yordam")

    await message.answer("\n".join(text))
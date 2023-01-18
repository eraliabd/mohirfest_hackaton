from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Oluvchi'),
            KeyboardButton(text='Xayriya'),
        ],
    ],
    resize_keyboard=True
)

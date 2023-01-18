from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

contact_button = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Contact', request_contact=True),
        ],
    ],
    resize_keyboard=True
)

location_button = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Location', request_location=True),
        ],
    ],
    resize_keyboard=True
)

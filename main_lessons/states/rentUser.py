from aiogram.dispatcher.filters.state import State, StatesGroup


class RentData(StatesGroup):
    full_name = State()
    phone_number = State()
    job = State()
    address = State()
    photo_id = State()
    compute_info = State()

from aiogram.dispatcher.filters.state import State, StatesGroup


class ReceiverData(StatesGroup):
    full_name = State()
    age = State()
    phone_number = State()
    address = State()
    job = State()
    # maqsadi
    purpose = State()

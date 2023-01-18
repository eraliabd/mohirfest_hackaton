from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command, Regexp
from aiogram.types import ReplyKeyboardRemove
from aiogram.types import Message, CallbackQuery

from pathlib import Path
# Kelgan hujjatlar (rasm/video/audio...) downloads/categories papkasiga tushadi
from keyboards.default.menuKeyboard import menu

download_path = Path().joinpath("downloads", "categories")
download_path.mkdir(parents=True, exist_ok=True)
# await message.video.download(destination=download_path)

from states.personalData import ReceiverData
from data.config import ADMINS, CHANNEL_ID

from loader import dp, db, bot


@dp.message_handler(Command('anketa'), state=None)
async def enter_test(message: types.Message):
    await message.answer("Ism va familiyangiz?", reply_markup=ReplyKeyboardRemove())
    await ReceiverData.full_name.set()


@dp.message_handler(state=ReceiverData.full_name)
async def answer_full_name(message: types.Message, state: FSMContext):
    full_name = message.text

    await state.update_data(
        {"full_name": full_name}
    )
    await message.answer("Yoshingiz?")
    await ReceiverData.next()  # next() - metodi keyingi holatga o'tkazadi
    # await PersonalData.username.set() - shu tartibda ham foydalanish mumkin


@dp.message_handler(state=ReceiverData.age)
async def answer_age(message: types.Message, state: FSMContext):
    age = message.text

    await state.update_data(
        {"age": age}
    )
    await message.answer("Telefon raqamingiz?\n\nMasalan: +998910019999")
    await ReceiverData.next()


@dp.message_handler(state=ReceiverData.phone_number)
async def answer_phone_number(message: types.Message, state: FSMContext):
    phone_number = message.text

    await state.update_data(
        {"phone_number": phone_number}
    )
    await message.answer("Manzilingiz?")
    await ReceiverData.next()


@dp.message_handler(state=ReceiverData.address)
async def answer_address(message: types.Message, state: FSMContext):
    address = message.text

    await state.update_data(
        {"address": address}
    )
    await message.answer("Kasbingiz?\n\nMasalan: Maktab o'quvchisi")
    await ReceiverData.next()


@dp.message_handler(state=ReceiverData.job)
async def answer_job(message: types.Message, state: FSMContext):
    job = message.text

    await state.update_data(
        {"job": job}
    )
    await message.answer("Maqsadingiz?")
    await ReceiverData.next()


@dp.message_handler(state=ReceiverData.purpose)
async def answer_purpose(message: types.Message, state: FSMContext):
    purpose = message.text

    await state.update_data(
        {"purpose": purpose}
    )
    # await message.answer("Ma'lumotlaringiz muaffaqiyatli yuborildi.")

    # Ma'lumotlarni qayta o'qiymiz
    data = await state.get_data()
    # print(data)
    full_name = data.get('full_name')
    age = data.get("age")
    phone_number = data.get("phone_number")
    address = data.get('address')
    job = data.get("job")
    purpose = data.get("purpose")

    # await db.create()
    # await db.create_table_users()
    await db.add_user(
        full_name=full_name, age=int(age), phone_number=phone_number, address=address, job=job, purpose=purpose
    )

    msg = "Quyidagi ma'lumotlar qabul qilindi:\n\n" \
          f"👨 O'quvchi: {full_name}\n" \
          f"🕙 Yosh: {age}\n" \
          f"📞 Bog'lanish: {phone_number}\n" \
          f"🌐 Manzil: {address}\n" \
          f"👨‍💻 Kasbi: {job}\n" \
          f"🚀 Maqsad: {purpose}\n\n" \
          f"🔗 @ula_shing"
    await message.answer(msg, reply_markup=menu)
    # await message.answer("Barcha ma'lumotlar to'g'rimi?")

    msg_channel = "#Oluvchi\n\n" \
                  f"👨 O'quvchi: {full_name}\n" \
                  f"🕙 Yosh: {age}\n" \
                  f"📞 Bog'lanish: {phone_number}\n" \
                  f"🌐 Manzil: {address}\n" \
                  f"👨‍💻 Kasbi: {job}\n" \
                  f"🚀 Maqsad: {purpose}\n\n" \
                  f"🔗 @ula_shing"
    await dp.bot.send_message(chat_id=ADMINS[0], text=msg_channel)

    # holatdan chiqib ketishning 2 xil usuli
    await state.finish()
    # await state.reset_state(with_data=False)

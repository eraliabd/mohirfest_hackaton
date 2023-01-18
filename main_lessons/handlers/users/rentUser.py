from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command, Regexp
from aiogram.types import ReplyKeyboardRemove, ContentType
from pathlib import Path

from keyboards.default.menuKeyboard import menu
from states.rentUser import RentData
from data.config import ADMINS, CHANNEL_ID

from loader import dp, db, bot

download_path = Path().joinpath("downloads", "charities")
download_path.mkdir(parents=True, exist_ok=True)


@dp.message_handler(Command('rent'), state=None)
async def enter_rent(message: types.Message):
    await message.answer("Ism va familiyangiz?", reply_markup=ReplyKeyboardRemove())
    await RentData.full_name.set()


from keyboards.default.startKeyboard import contact_button
@dp.message_handler(state=RentData.full_name)
async def rent_full_name(message: types.Message, state: FSMContext):
    full_name = message.text

    await state.update_data(
        {"full_name": full_name}
    )
    await message.answer("Telefon raqamingiz?\n\nMasalan: +998910019999", reply_markup=contact_button)
    await RentData.next()

PHONE_NUMBER = r"^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$"
@dp.message_handler(state=RentData.phone_number)
@dp.message_handler(Regexp(PHONE_NUMBER))
async def rent_phone_number(message: types.Message, state: FSMContext):
    phone_number_text = message.text
    phone_number = message.contact.phone_number
    print(phone_number)

    await state.update_data(
        {"phone_number": phone_number, "phone_number_text": phone_number_text}
    )
    await message.answer("Kasbingiz?", reply_markup=ReplyKeyboardRemove())
    await RentData.next()


@dp.message_handler(state=RentData.job)
async def rent_job(message: types.Message, state: FSMContext):
    job = message.text

    await state.update_data(
        {"job": job}
    )
    await message.answer("Manzilingiz?")
    await RentData.next()


@dp.message_handler(state=RentData.address)
async def rent_address(message: types.Message, state: FSMContext):
    address = message.text

    await state.update_data(
        {"address": address}
    )
    await message.answer("Shaxsiy rasm?")
    await RentData.next()


@dp.message_handler(content_types=ContentType.PHOTO, state=RentData.photo_id)
async def rent_photo(message: types.Message, state: FSMContext):
    photo_down = await message.photo[-1].download()
    # print(photo_down)
    photo_id = message.photo[-1].file_id

    await state.update_data(
        {"photo_id": photo_id}
    )
    await message.answer("Kompyuter yoki pul xayriya qilasizmi? Shu haqida biroz ma'lumot bering.")
    await RentData.next()


@dp.message_handler(state=RentData.compute_info)
async def rent_info(message: types.Message, state: FSMContext):
    compute_info = message.text

    await state.update_data(
        {"compute_info": compute_info}
    )
    # await message.answer("Ma'lumotlaringiz muaffaqiyatli yuborildi.")

    # Ma'lumotlarni qayta o'qiymiz
    data = await state.get_data()
    # print(data)
    full_name = data.get('full_name')
    phone_number = data.get("phone_number")
    job = data.get("job")
    address = data.get('address')
    photo_id = data.get("photo_id")
    compute_info = data.get("compute_info")

    await db.add_user1(
        full_name=full_name, phone_number=phone_number, job=job, address=address, photo_id=photo_id,
        compute_info=compute_info
    )

    msg = "Quyidagi ma'lumotlar qabul qilindi:\n\n" \
          f"👨 Xayriyachi: {full_name}\n" \
          f"📞 Bog'lanish: {phone_number}\n" \
          f"👨‍💻 Kasbi: {job}\n" \
          f"🌐 Manzil: {address}\n" \
          f"📋 Ma'lumot: {compute_info}\n\n" \
          f"🔗 @ula_shing"
    await message.answer_photo(photo=photo_id, caption=msg, reply_markup=menu)

    msg_channel = "#Xayriya\n\n" \
                  f"👨 Xayriyachi: {full_name}\n" \
                  f"📞 Bog'lanish: {phone_number}\n" \
                  f"👨‍💻 Kasbi: {job}\n" \
                  f"🌐 Manzil: {address}\n" \
                  f"📋 Ma'lumot: {compute_info}\n\n" \
                  f"🔗 @ula_shing"
    await dp.bot.send_photo(chat_id=ADMINS[0], photo=photo_id, caption=msg_channel)

    await state.finish()

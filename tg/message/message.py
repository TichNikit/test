import asyncio

from aiogram import types, Dispatcher, F
from aiogram.filters import CommandStart

from db.database import get_planes
from get_data import get_planes_data
from tg.keybord.kb import keyboard_start


async def start_command(message: types.Message):
    await message.answer(f'Привет {message.from_user.full_name}', reply_markup=keyboard_start)


async def get_data(callback_query: types.CallbackQuery):
    await callback_query.answer()
    result_list = ''
    result = await get_planes_data()
    await callback_query.message.answer("Данные о Китайских самолетах:")
    for flight in result:
        flight_id = flight['flightid']
        registration = flight['extraInfo']['reg']
        item_text = f"Flight ID: {flight_id},  Reg: {registration}"
        result_list = result_list + item_text + '\n'
        message_text = f"{result_list}"
        if len(message_text) > 4096:
            for i in range(0, len(message_text), 4096):
                await callback_query.message.answer(message_text[i:i + 4096])
                await asyncio.sleep(2)
        else:
            await callback_query.message.answer(message_text)

    await callback_query.message.answer("Другие возможности", reply_markup=keyboard_start)


async def get_all_from_db(callback_query: types.CallbackQuery):
    await callback_query.answer()
    result_list = ''
    result = get_planes()
    await callback_query.message.answer("Данные из базы данных:")
    for flight in result:
        flight_id = flight[1]
        registration = flight[2]
        item_text = f"Flight ID: {flight_id},  Reg: {registration}"
        result_list = result_list + item_text + '\n'
        message_text = f"{result_list}"
        if len(message_text) > 4096:
            for i in range(0, len(message_text), 4096):
                await callback_query.message.answer(message_text[i:i + 4096])
                await asyncio.sleep(5)
        else:
            await callback_query.message.answer(message_text)

    await callback_query.message.answer("Другие возможности", reply_markup=keyboard_start)



def register_user_messages(dp: Dispatcher):
    dp.message.register(start_command, CommandStart())
    dp.callback_query.register(get_data, F.data == 'data')
    dp.callback_query.register(get_all_from_db, F.data == 'data_bd')

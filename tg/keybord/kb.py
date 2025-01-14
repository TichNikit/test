from aiogram import types

keyboard_start = [
    [types.InlineKeyboardButton(text="Получить сокращенные текущие данные", callback_data='data')],
    [types.InlineKeyboardButton(text="Полудить данные из базы данных", callback_data='data_bd')],]
keyboard_start = types.InlineKeyboardMarkup(inline_keyboard=keyboard_start)
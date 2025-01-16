import asyncio

from aiogram import types, Dispatcher, F
from aiogram.filters import CommandStart


async def start_command(message: types.Message):
    chat_id = message.chat.id
    await message.answer(f'Привет {message.from_user.full_name}')


async def ignore_message(message: types.Message):
    pass


def register_user_messages(dp: Dispatcher):
    dp.message.register(start_command, CommandStart())
    dp.message.register(ignore_message)

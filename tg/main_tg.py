import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties

from tg.message.message import register_user_messages
from tg.tokens import token

logger = logging.getLogger(__name__)


async def main():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    )
    logger.info("Starting bot")

    bot = Bot(token, default=DefaultBotProperties(parse_mode='HTML'))
    dp = Dispatcher()
    register_user_messages(dp)
    try:
        await dp.start_polling(bot)
    except Exception as e:
        logger.error(f"Failed to start polling: {e}")


if __name__ == '__main__':
    asyncio.run(main())
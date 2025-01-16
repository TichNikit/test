import asyncio
import logging

from sqlalchemy.exc import IntegrityError
from sqlalchemy import select, insert, delete

from app.db import SessionLocal, Planes
from tg.telegram_bot import send_message_to_telegram
from tg.tokens import id_bot

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class PlaneRepository:

    @classmethod
    async def get_all_planes(cls):
        async with SessionLocal() as session:
            task = select(Planes)
            result = await session.execute(task)
            planes = result.scalars().all()
            return planes

    @classmethod
    async def post_planes(cls, data):
        existing_flight = await cls.get_all_planes()
        existing_flight_ids = [flight.flightid for flight in existing_flight]
        async with SessionLocal() as session:
            total = 0
            for flight in data:
                if flight.flightid not in existing_flight_ids:
                    task = insert(Planes).values(
                        flightid=flight.flightid,
                        reg=flight.reg,
                    )
                    try:
                        await session.execute(task)
                        message = f"New Flight ID: {flight.flightid}, Reg: {flight.reg}"
                        send_message_to_telegram(id_bot, message)
                        total += 1
                        logger.info(f"Самолет добавлен в базу данных: {flight}")
                        await asyncio.sleep(0.5)
                    except IntegrityError as e:
                        await session.rollback()
                        logger.error(f"Ошибка: {e}. Пропуск записи с flightid={flight.flightid}.")
                        continue

            await session.commit()
            logger.info(f"Получена информация:\n {total} записей успешно добавлено.")
        return total

    @classmethod
    async def delete_all_planes(cls):
        async with SessionLocal() as session:
            task = delete(Planes)
            await session.execute(task)
            await session.commit()
            logger.info("Все записи успешно удалены из базы данных.")

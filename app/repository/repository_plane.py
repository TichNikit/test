import asyncio

from sqlalchemy.exc import IntegrityError
from sqlalchemy import select, insert

from app.db import SessionLocal, Planes
from get_data import get_planes_data


class PlaneRepository:

    @classmethod
    async def get_all_plans(cls):
        async with SessionLocal() as session:
            task = select(Planes)
            result = await session.execute(task)
            otw = result.scalars().all()
            return otw


    @classmethod
    async def post_planes(cls):
        async with SessionLocal() as session:
            total = 0
            data = await get_planes_data()
            for flight in data:

                task = insert(Planes).values(
                    flightid=flight['flightid'],
                    reg=flight['extraInfo']['reg'],
                )
                try:
                    await session.execute(task)
                    total += 1
                except IntegrityError:

                    await session.rollback()
                    continue
            await session.commit()
        print(total)
        return total
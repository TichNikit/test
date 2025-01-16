import asyncio
import logging
import httpx
from fr24.grpc import (
    live_feed_message_create,
    live_feed_post,
    live_feed_request_create,
)
from google.protobuf.json_format import MessageToDict

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


async def get_planes_data():
    async with httpx.AsyncClient() as client:
        message = live_feed_message_create(north=81, south=41, west=19, east=169)
        request = live_feed_request_create(message)

        result = await live_feed_post(client, request)
        flights = MessageToDict(result)["flightsList"]

        logger.info(f"Найдено {len(flights)} самолетов в общем.")

        list_сhinese_planes = []

        for flight in flights:
            extra_info = flight.get('extraInfo')
            if extra_info and extra_info.get('reg'):
                if extra_info['reg'].startswith('B-'):
                    list_сhinese_planes.append(flight)

        logger.info(f"Получено {len(list_сhinese_planes)} китайских самолетов.")
        return list_сhinese_planes

# Вызов функции через asyncio.run()
# data = asyncio.run(get_planes_data())
# print(data)

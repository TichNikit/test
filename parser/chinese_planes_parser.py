import asyncio
import logging
import httpx
import requests
import time
from fr24.grpc import live_feed_message_create, live_feed_request_create, live_feed_post
from google.protobuf.json_format import MessageToDict


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


async def get_chinese_planes():
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
                    flight_id = flight['flightid']
                    registration = flight['extraInfo']['reg']
                    list_сhinese_planes.append({'flightid': flight_id, 'reg': registration})

        logger.info(f"Найдено {len(list_сhinese_planes)} китайских самолетов.")
        logger.debug(f"Список найденых китайских самолетов: {list_сhinese_planes}")

        return list_сhinese_planes


def sent_list_of_chinese(chinese_planes):
    try:
        response = requests.post("http://127.0.0.1:8000/planes", json={"planes": chinese_planes})
        response.raise_for_status()
    except requests.exceptions.HTTPError as err:
        print(f'HTTP error occurred: {err}')
    except Exception as e:
        print(f'An error occurred: {e}')


while True:
    chinese_planes = asyncio.run(get_chinese_planes())
    sent_list_of_chinese(chinese_planes)
    time.sleep(3600)

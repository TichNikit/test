import asyncio
import requests
import time

from get_data import get_planes_data


def get_list_of_chinese():
    data = asyncio.run(get_planes_data())
    list_сhinese_planes = []

    for flight in data:
        flight_id = flight['flightid']
        registration = flight['extraInfo']['reg']
        res = {'flightid': flight_id, 'reg': registration}
        list_сhinese_planes.append(res)
    print(list_сhinese_planes)
    return list_сhinese_planes


def sent_list_of_chinese(chinese):
    try:
        response = requests.post("http://127.0.0.1:8000/planes", json={"planes": chinese})
        response.raise_for_status()
    except requests.exceptions.HTTPError as err:
        print(f'HTTP error occurred: {err}')
    except Exception as e:
        print(f'An error occurred: {e}')

while True:
    result = get_list_of_chinese()
    sent_list_of_chinese(result)
    time.sleep(3600)

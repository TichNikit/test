import logging
import requests
from tg.tokens import token


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
TELEGRAM_API_URL = f"https://api.telegram.org/bot{token}/sendMessage"


def send_message_to_telegram(chat_id, message):
    url = TELEGRAM_API_URL.format(token=f'{token}')
    payload = {
        'chat_id': chat_id,
        'text': message,
        'parse_mode': 'HTML'
    }
    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()
    except requests.exceptions.HTTPError as err:
        logger.info(f"Ошибка при отправке сообщения в Telegram: {err}")

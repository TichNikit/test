import requests

from tg.tokens import token

TELEGRAM_API_URL = f"https://api.telegram.org/bot{token}/sendMessage"

def send_message_to_telegram(chat_id, message):
    url = TELEGRAM_API_URL.format(token=f'{token}')  # Замените на ваш токен
    payload = {
        'chat_id': chat_id,  # Замените на ваш chat_id
        'text': message,
    }
    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()
    except requests.exceptions.HTTPError as err:
        print(f"Ошибка при отправке сообщения в Telegram: {err}")
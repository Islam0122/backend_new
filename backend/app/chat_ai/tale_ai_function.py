import base64
import json
import os
import uuid
from typing import Any

import requests
from requests.auth import HTTPBasicAuth

CLIENT_ID='71b92890-bf91-4b6b-9645-6561b93e3d7d'
SECRET='3278c7e4-6c0c-4b7b-a8b7-9baadb679504'


def get_access_token() -> Any | None:
    url = "https://ngw.devices.sberbank.ru:9443/api/v2/oauth"
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept': 'application/json',
        'RqUID': str(uuid.uuid4()),  # уникальный идентификатор запроса
    }
    payload = {"scope": "GIGACHAT_API_PERS"}

    try:
        res = requests.post(
            url=url,
            headers=headers,
            auth=HTTPBasicAuth(CLIENT_ID, SECRET),
            data=payload,
            verify=False,  # Убедитесь, что использование verify=False безопасно для вашей среды
        )
        res.raise_for_status()  # проверка на наличие ошибок
        access_token = res.json().get("access_token")
        if not access_token:
            raise ValueError("Токен доступа не был получен.")
        return access_token
    except requests.RequestException as e:
        print("Ошибка при получении access token:", e)
        return None


def send_prompt(msg: str, access_token: str):
    url = "https://gigachat.devices.sberbank.ru/api/v1/chat/completions"
    payload = json.dumps({
        "model": "GigaChat",
        "messages": [
            {
                "role": "user",
                "content": msg,
            }
        ],
    })
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'Authorization': f'Bearer {access_token}'
    }

    try:
        response = requests.post(url, headers=headers, data=payload, verify=False)
        response.raise_for_status()  # проверка на наличие ошибок
        return response.json()["choices"][0]["message"]["content"]
    except requests.RequestException as e:
        print("Ошибка при отправке запроса к GigaChat API:", e)
        return "Ошибка при получении ответа от GigaChat."


def sent_prompt_and_get_response(msg: str, language: str):
    access_token = get_access_token()

    # Создаем сообщение в зависимости от языка
    messages = {
        "ru": f'✨🌈 Придумай необычную, уникальную сказку о {msg} 🧚‍♀️🦄! Пусть это будет история, где царства превращаются в нечто удивительное, а герои сталкиваются с необычными событиями и открытиями 🌟🌌. Больше чудес и смайликов! 😍🎭',
        "en": f'✨🌈 Create an extraordinary, unique fairy tale about {msg} 🧚‍♀️🦄! Let it be a story where kingdoms turn into something marvelous, and heroes face unusual events and discoveries 🌟🌌. Add more wonders and emojis! 😍🎭'
    }

    # Получаем сообщение в зависимости от языка, по умолчанию используется русский
    message = messages.get(language, messages["ru"])

    # Проверка наличия access token
    if access_token:
        # Получаем ответ от send_prompt и добавляем смайлики
        response = send_prompt(message, access_token)
        decorated_response = f'✨🌟 {response} 🌈🧚‍♂️'
        return decorated_response
    else:
        return "Не удалось получить access token."



def sent_prompt_with_photo_and_get_response(photo, language: str):
    access_token = get_access_token()
    return "🚧 Эта команда пока недоступна. Вернитесь в меню /start 😊"

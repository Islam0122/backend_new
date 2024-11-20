from .env_reader import env

CORS_ALLOW_METHODS = [
    'DELETE',
    'GET',
    'OPTIONS',
    'PATCH',
    'POST',
    'PUT',
]

CORS_ALLOW_HEADERS = [
    'accept',
    'accept-encoding',
    'authorization',
    'content-type',
    'accept-language',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
]
# CORS_ALLOW_ALL_ORIGINS = True
#
# # CORS_ORIGIN_ALLOW_ALL = True # Отключаем разрешение всех доменов
# CORS_ALLOWED_ORIGINS = [
#     "http://127.0.0.1:5500/index.html",
#      "http://127.0.0.1:5500",  # порт Go Live
#     "http://localhost:5500",  # если Go Live работает на localhost
#     "http://localhost:63343",  # Your local frontend
#         "https://duishobaevislam01.up.railway.app",  # ваш сервер на Railway
# ]
CORS_ORIGIN_WHITELIST = [
    # "http://127.0.0.1:5500/index.html",
    'http://127.0.0.1:8000',
    "http://127.0.0.1:5500",  # порт Go Live
    "http://localhost:5500",  # если Go Live работает на localhost
    "http://localhost:63343",  # Your local frontend
    "http://localhost:63342",  # Your local frontend
    "https://duishobaevislam01.up.railway.app",  # ваш сервер на Railway
]

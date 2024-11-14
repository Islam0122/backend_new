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

# CORS_ORIGIN_ALLOW_ALL = False  # Отключаем разрешение всех доменов
# CORS_ALLOWED_ORIGINS = [
#     "http://localhost:63343",  # Your local frontend
#     "https://duishobaevislam01.up.railway.app",  # Your backend URL
# ]
CORS_ORIGIN_WHITELIST = [
    "http://localhost:63343",  # Your local frontend
    "https://duishobaevislam01.up.railway.app",  # Your backend URL
]
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

# CORS_ALLOWED_ORIGINS = env('CORS_ALLOWED_ORIGINS', cast=csv())
CORS_ORIGIN_ALLOW_ALL = True
# CORS_ALLOWED_ORIGINS = [
#     "http://localhost:*",  # Разрешаем доступ с любых портов на localhost
#     "https://duishobaevislam01.up.railway.app",  # Разрешаем доступ с продакшн сервера
# ]
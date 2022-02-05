"""Константы"""
import logging

# Порт по умолчанию для сетевого ваимодействия
DEF_PORT = 7779
# IP адрес по умолчанию для подключения клиента
DEF_IP_ADDRESS = '127.0.0.1'
# Максимальная очередь подключений
MAX_CONNECTIONS = 10
# Максимальная длинна сообщения в байтах
MAX_PACKAGE_LENGTH = 2048
# Кодировка проекта
FORMAT = 'utf-8'

# Прококол JIM основные ключи:
ACTION = 'action'
CURRENT_TIME = 'time'
USER = 'user'
ACCOUNT_LOGIN = 'account_name'
SENDER = 'sender'

# Прочие ключи, используемые в протоколе
CODE_PRESENCE = 'presence'
CODE_RESPONSE = 'response'
CODE_ERROR = 'error'
MESSAGE = 'message'
MESSAGE_TEXT = 'mess_text'


LOGGING_LEVEL = logging.DEBUG
"""Программа-клиент"""

import sys, json, socket, time
from common.variables import ACCOUNT_LOGIN, USER,CURRENT_TIME, ACTION,DEF_PORT, DEF_IP_ADDRESS, MAX_CONNECTIONS, MAX_PACKAGE_LENGTH, FORMAT, CODE_RESPONSE, CODE_ERROR, CODE_PRESENCE
from common.utils import get_message, send_message


def create_answer(account_login='Guest'):
    '''
    Функция генерирует запрос о присутствии клиента
    :param account_name:
    :return:
    '''
    # {'action': 'presence', 'time': 'Sat Jan 22 21:02:04 2022', 'user': {'account_name': 'Guest'}}
    data = {
        ACTION: CODE_PRESENCE,
        CURRENT_TIME: time.ctime(),
        USER: {
            ACCOUNT_LOGIN: account_login
        }
    }
    return data


def process_answer(message):
    '''
    Функция разбирает ответ сервера
    :param message:
    :return:
    '''
    if CODE_RESPONSE in message:
        if message[CODE_RESPONSE] == 200:
            return f'Ответ сервера: {message[CODE_RESPONSE]} OK'
        return f'Ответ сервера: 400 : {message[CODE_ERROR]}'
    raise ValueError


def base():
    '''Загружаем параметы коммандной строки'''
    # client.py 192.168.1.2 8079
    try:
        server_address = sys.argv[1]
        server_port = int(sys.argv[2])
        if server_port < 1024 or server_port > 65535:
            raise ValueError
    except IndexError:
        server_address = DEF_IP_ADDRESS
        server_port = DEF_PORT
    except ValueError:
        print('В качестве порта может быть указано только число в диапазоне от 1024 до 65535.')
        sys.exit(1)

    # Инициализация сокета и обмен

    new_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    new_socket.connect((server_address, server_port))
    message_to_server = create_answer()
    send_message(new_socket, message_to_server)
    try:
        answer = process_answer(get_message(new_socket))
        print(answer)
    except (ValueError, json.JSONDecodeError):
        print(f'Не удалось декодировать сообщение сервера.')


if __name__ == '__main__':
    base()

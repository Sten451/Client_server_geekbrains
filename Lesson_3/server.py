"""Программа-сервер"""

import socket, sys, json
from common.variables import ACCOUNT_LOGIN, USER,CURRENT_TIME, ACTION,DEF_PORT, DEF_IP_ADDRESS, \
    MAX_CONNECTIONS, CODE_RESPONSE, CODE_ERROR, CODE_PRESENCE
from common.utils import get_message, send_message


def process_client_message(message):
    '''
    Обработчик сообщений от клиентов, принимает словарь -
    сообщение от клинта, проверяет корректность,
    возвращает словарь-ответ для клиента

    :param message:
    :return:
    '''
    if ACTION in message and message[ACTION] == CODE_PRESENCE and CURRENT_TIME in message \
            and USER in message and message[USER][ACCOUNT_LOGIN] == 'Guest':
        return {CODE_RESPONSE: 200}
    return {
        CODE_RESPONSE: 400,
        CODE_ERROR: 'Bad Request'
    }


def base():
    '''
    Загрузка параметров командной строки, если нет параметров, то задаём значения по умоланию.
    Сначала обрабатываем порт:
    server.py -p 8079 -a 192.168.1.2
    :return:
    '''

    try:
        if '-p' in sys.argv:
            port = int(sys.argv[sys.argv.index('-p') + 1])
        else:
            port = DEF_PORT
        if port < 1024 or port > 65535:
            raise ValueError
    except IndexError:
        print(f'После параметра -\'p\' необходимо указать номер порта.')
        sys.exit(1)
    except ValueError:
        print(f'В качастве порта может быть указано только число в диапазоне от 1024 до 65535.')
        sys.exit(1)

    # Затем загружаем какой адрес слушать

    try:
        if '-a' in sys.argv:
            address = sys.argv[sys.argv.index('-a') + 1]
        else:
            address = ''

    except IndexError:
        print(f'После параметра \'a\'- необходимо указать адрес, который будет слушать сервер.')
        sys.exit(1)

    # Готовим сокет

    new_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    new_socket.bind((address, port))

    # Слушаем порт

    new_socket.listen(MAX_CONNECTIONS)

    while True:
        client, client_address = new_socket.accept()
        try:
            message_from_cient = get_message(client)
            print(f'{message_from_cient}')
            # {'action': 'presence', 'time': 'Sat Jan 22 23:25:10 2022', 'user': {'account_name': 'Guest'}}
            response = process_client_message(message_from_cient)
            send_message(client, response)
            client.close()
        except (ValueError, json.JSONDecodeError):
            print(f'Принято некорретное сообщение от клиента.')
            client.close()


if __name__ == '__main__':
    base()

"""Утилиты"""

import json
from common.variables import MAX_PACKAGE_LENGTH, FORMAT
from errors import IncorrectDataRecivedError, NonDictInputError
from decoration import log


@log
def get_message(client):
    encoded_response = client.recv(MAX_PACKAGE_LENGTH)
    if isinstance(encoded_response, bytes):
        json_response = encoded_response.decode(FORMAT)
        response = json.loads(json_response)
        if isinstance(response, dict):
            return response
        raise IncorrectDataRecivedError
    raise IncorrectDataRecivedError


@log
def send_message(sock, message):
    if not isinstance(message, dict):
        raise NonDictInputError
    sock.send(json.dumps(message).encode(FORMAT))

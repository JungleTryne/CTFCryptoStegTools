from CryptoModule.console_constants import HELP_MESSAGE, FILE_NOT_FOUND
from CryptoModule.crypto_tools import CesarCypherTools, VernamCypherTools, VigenereCypherTools
from CryptoModule.console_exceptions import UnknownArgument


def get_text(file_path: str) -> str:
    try:
        with open(file_path, 'r') as file:
            file_text = file.read()
            return file_text
    except:
        raise FileNotFoundError


def is_key_required(function) -> bool:
    key_required = [
        CesarCypherTools.encode,
        CesarCypherTools.decode,
        VigenereCypherTools.encode,
        VigenereCypherTools.decode,
        VernamCypherTools.decode
    ]
    return function in key_required


def get_function(main_argument):
    ways = {
        '-Ce': CesarCypherTools.encode,
        '-Cd': CesarCypherTools.decode,
        '-Ch': CesarCypherTools.frequency_analise_hack,
        '-Ve': VigenereCypherTools.encode,
        '-Vd': VigenereCypherTools.decode,
        '-VVe': VernamCypherTools.encode,
        '-VVd': VernamCypherTools.decode
    }
    try:
        function = ways[main_argument]
        return function
    except:
        raise UnknownArgument


def handle_request(parameters: list) -> str:
    try:
        file_path = parameters[1]
        main_argument = parameters[2]
    except:
        return HELP_MESSAGE

    try:
        file_text = get_text(file_path)
    except:
        return FILE_NOT_FOUND

    try:
        function = get_function(main_argument)
    except UnknownArgument:
        return HELP_MESSAGE

    if is_key_required(function):
        with open(parameters[3], 'r') as file:
            key = file.read()
        answer = function(file_text, key)
        return answer
    else:
        answer = function(file_text)
        return answer

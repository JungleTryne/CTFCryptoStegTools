from CryptoModule.console_constants import HELP_MESSAGE, FILE_NOT_FOUND
from CryptoModule.crypto_tools import CesarCypherTools, VernamCypherTools, VigenereCypherTools
from CryptoModule.console_exceptions import UnknownArgument


def get_text(file_path: str) -> str:
    with open(file_path, 'r') as file:
        file_text = file.read()
        return file_text


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
    except IndexError:
        raise UnknownArgument


def handle_request(parameters: list):
    try:
        file_path = parameters[1]
        main_argument = parameters[2]
    except IndexError:
        print(HELP_MESSAGE)
        return '', None

    try:
        file_text = get_text(file_path)
    except FileNotFoundError:
        print(FILE_NOT_FOUND)
        return '', None

    output_file = None

    try:
        function = get_function(main_argument)
    except UnknownArgument:
        print(HELP_MESSAGE)
        return '', None

    if is_key_required(function):
        try:
            if parameters[4] == '--output':
                output_file = parameters[5]
        except IndexError:
            pass
    else:
        try:
            if parameters[3] == '--output':
                output_file = parameters[5]
        except IndexError:
            pass

    if is_key_required(function):
        with open(parameters[3], 'r') as file:
            key = file.read()
        answer = function(file_text, key)
        return answer, output_file
    else:
        answer = function(file_text)
        return answer, output_file

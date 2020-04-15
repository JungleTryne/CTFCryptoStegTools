import string
from crypto_constants import LETTER_FREQUENCY
from random import randint


def lower_arguments(func):
    def wrapper(*args, **kwargs):
        new_args = []
        for i in range(len(args)):
            if isinstance(args[i], str):
                new_args.append(args[i].lower())
            else:
                new_args.append(args[i])
        args = tuple(new_args)
        for key in kwargs:
            if isinstance(kwargs[key], str):
                kwargs[key] = kwargs[key].lower()
        return func(*args, **kwargs)

    wrapper.__name__ = func.__name__
    wrapper.__doc__ = func.__doc__
    wrapper.__module__ = func.__module__

    return wrapper


class CesarCypherTools:
    @staticmethod
    @lower_arguments
    def encode(message: str, key: int):
        key = int(key)
        return CesarCypherTools.rotate_text(message, key)

    @staticmethod
    @lower_arguments
    def decode(message: str, key: int):
        key = int(key)
        return CesarCypherTools.rotate_text(message, 26 - key)

    @staticmethod
    def get_delta(message_counter: dict) -> int:
        delta = 0
        for char in message_counter:
            delta += (message_counter[char] - LETTER_FREQUENCY[char]) ** 2
        return delta

    @staticmethod
    def rotate_counter(message_counter: dict) -> None:
        values = []
        for i in range(len(string.ascii_lowercase)):
            values.append(message_counter[string.ascii_lowercase[i]])

        new_values = values[-1:] + values[:-1]
        for i in range(len(string.ascii_lowercase)):
            message_counter[string.ascii_lowercase[i]] = new_values[i]
        pass

    @staticmethod
    def rotate_text(message: str, key: int) -> str:
        solution = ''
        for char in message:
            if char in string.ascii_lowercase:
                solution += chr(((ord(char) - 97 + key) % 26) + 97)
            else:
                solution += char
        return solution

    @staticmethod
    @lower_arguments
    def frequency_analise_hack(message: str) -> str:
        """
        Метод расшифровки сообщения методом частотного анализа
        :param message: зашифрованное сообщение
        :return: расшифрованное сообщение
        """
        if not message:
            return ""
        counter = dict()
        for char in string.ascii_lowercase:
            counter[char] = 0
        total = 0

        for char in message:
            if char in string.ascii_lowercase:
                counter[char] += 1
                total += 1

        for key in counter:
            counter[key] /= total
            counter[key] *= 100

        delta = CesarCypherTools.get_delta(counter)
        rotate_solution = 0

        for i in range(25):
            CesarCypherTools.rotate_counter(counter)
            new_delta = CesarCypherTools.get_delta(counter)
            if new_delta < delta:
                rotate_solution = i + 1
                delta = new_delta

        return CesarCypherTools.rotate_text(message, rotate_solution)


class VigenereCypherTools:
    @staticmethod
    def encode_symbol(char: str, key_char: str):
        return chr(
            ((ord(char) - ord('a') +
              ord(key_char) - ord('a')) % 26) + ord('a')
        )

    @staticmethod
    def decode_symbol(char: str, key_char: str):
        return chr(
            ((ord(char) - ord('a') -
              ord(key_char) + ord('a')) % 26) + ord('a')
        )

    @staticmethod
    def enlarge_key(message: str, key: str) -> str:
        """
        Возвращает ключ той же длины, что и сообщение, путем "копипасты"
        :param message: сообщение
        :param key: ключ
        :return: удлиннёный ключ
        """
        longer_key = key
        pointer = 0
        while len(longer_key) < len(message):
            longer_key += key[pointer]
            pointer = (pointer + 1) % len(key)
        return longer_key

    @staticmethod
    @lower_arguments
    def encode(message: str, key: str) -> str:
        """
        Метод шифрования сообщения методом Вижера
        :param message: сообщения для шифровки
        :param key: ключ шифрования
        :return: зашифрованное сообщение
        """
        longer_key = VigenereCypherTools.enlarge_key(message, key)
        encrypted = ''
        for i in range(len(message)):
            encrypted += VigenereCypherTools.encode_symbol(message[i], longer_key[i])
        return encrypted

    @staticmethod
    @lower_arguments
    def decode(message: str, key: str) -> str:
        """
        Функция декодирования сообщения
        :param message: зашифрованное сообщение
        :param key: ключ шифрования
        :return: расшифрованное сообщение
        """
        longer_key = VigenereCypherTools.enlarge_key(message, key)
        decrypted = ''
        for i in range(len(message)):
            decrypted += VigenereCypherTools.decode_symbol(message[i], longer_key[i])
        return decrypted


class VernamCypherTools:
    @staticmethod
    def encode_symbol(char: str, key_char: str):
        return chr((ord(char) + ord(key_char) % 256))

    @staticmethod
    def decode_symbol(char: str, key_char: str):
        return chr((ord(char) - ord(key_char) % 256))

    @staticmethod
    def generate_key(message: str) -> str:
        """
        Функция генерации ключа для сообщения
        :param message: сообщение
        :return: ключ
        """
        key_length = len(message)
        key = ''
        for i in range(key_length):
            key += chr(randint(0, 255))
        return key

    @staticmethod
    def encode(message) -> tuple:
        """
        Функция шифрования сообщения методом Вернама. Ключ генерируется автоматически
        :param message: сообщение для шифрования
        :return: зашифрованное сообщение и ключ
        """
        key = VernamCypherTools.generate_key(message)
        encrypted = ''
        for i in range(len(message)):
            encrypted += VernamCypherTools.encode_symbol(message[i], key[i])
        return encrypted, key

    @staticmethod
    def decode(encrypted, key):
        """
        Функция расшифровки сообщения сетодом Вернама
        :param encrypted: зашифрованное сообщение
        :param key: ключ шифрования
        :return: расшифрованное сообщение
        """
        message = ''
        for i in range(len(encrypted)):
            message += VernamCypherTools.decode_symbol(encrypted[i], key[i])
        return message

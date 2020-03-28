import string
from crypto_constants import LETTER_FREQUENCY


class CesarCypherSolver:
    @staticmethod
    def get_delta(message_counter: dict) -> int:
        delta = 0
        for char in message_counter:
            delta += (message_counter[char] - LETTER_FREQUENCY[char])**2
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
                solution += chr(((ord(char)-97 + key) % 26) + 97)
            else:
                solution += char
        return solution

    @staticmethod
    def frequency_analise_hack(message: str) -> str:
        """
        Метод расшифровки сообщения методом частотного анализа
        :param message: зашифрованное сообщение
        :return: расшифрованное сообщение
        """
        if not message:
            return ""
        message = message.lower()
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

        delta = CesarCypherSolver.get_delta(counter)
        rotate_solution = 0

        for i in range(25):
            CesarCypherSolver.rotate_counter(counter)
            new_delta = CesarCypherSolver.get_delta(counter)
            if new_delta < delta:
                rotate_solution = i+1
                delta = new_delta

        return CesarCypherSolver.rotate_text(message, rotate_solution)


class VigenereCypherSolver:
    pass

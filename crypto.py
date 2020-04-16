from CryptoModule import console_handler as handler
import sys


def main():
    arguments = sys.argv
    answer = handler.handle_request(arguments)
    if isinstance(answer, tuple):
        with open("output.txt", 'w+') as file:
            file.write(str(answer[0]))
        with open("key.txt", 'w+') as file:
            file.write(str(answer[1]))
    else:
        with open("output.txt", 'w+') as file:
            file.write(str(answer))


if __name__ == '__main__':
    main()
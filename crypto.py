from CryptoModule import console_handler as handler
import sys


def main():
    arguments = sys.argv
    answer, output_file = handler.handle_request(arguments)
    if output_file is None:
        print(answer)
    elif isinstance(answer, tuple):
        with open("{0}".format(output_file), 'w+') as file:
            file.write(str(answer[0]))
        with open("key.txt", 'w+') as file:
            file.write(str(answer[1]))
    else:
        with open("{0}".format(output_file), 'w+') as file:
            file.write(str(answer))


if __name__ == '__main__':
    main()
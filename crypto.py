import console_handler as handler
import sys
import crypto_tools

def main():
    arguments = sys.argv
    answer = handler.handle_request(arguments)


if __name__ == '__main__':
    main()
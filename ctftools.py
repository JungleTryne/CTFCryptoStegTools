from crypto_tools import CesarCypherTools
from crypto_tools import VigenereCypherTools
from crypto_tools import VernamCypherTools


def main():
    solution = VernamCypherTools.encode('hello world')
    solution = VernamCypherTools.decode(*solution)
    print(solution)


if __name__ == '__main__':
    main()
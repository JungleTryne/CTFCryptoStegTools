from crypto_tools import CesarCypherSolver
from crypto_tools import VigenereCypherSolver

def main():
    text = "ATTACKATDAWN"
    key = "LEMON"
    solution = VigenereCypherSolver.encode(text, key)
    solution = VigenereCypherSolver.decode(solution, key)
    print(solution)


if __name__ == '__main__':
    main()
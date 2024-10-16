import random
from string import ascii_letters, digits, punctuation

SYMBOLS = ascii_letters + digits + punctuation


def get_password(n=32):
    result = ""
    while len(result) < n:
        symbol = random.choice(SYMBOLS)
        if symbol in result:
            continue
        result += symbol

    return result


def main() -> None:
    random.seed()
    print(f"Password: {get_password()}")


if __name__ == '__main__':
    main()
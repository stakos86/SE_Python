import random
from string import ascii_letters, digits, punctuation

SYMBOLS = ascii_letters + digits + punctuation


def get_password(n: int = 32) -> str:
    result: str = ""
    # counter int = 0

    while len(result) < n:
        symbol: str = random.choice(SYMBOLS)
        if symbol in result:
            continue
        result += symbol

    return result


def main() -> None:
    random.seed()
    password: str = get_password()

    print(f"password: {password}")
    print(f"it is{' not' if len(set(list(password))) != len(password) else ''} unique")


if __name__ == '__main__':
    main()
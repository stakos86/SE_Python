import random


def divide(a: int, b: int):
    """

    :param a: делимое
    :param b: делитель
    :return: результат
    """
    print(a / b)


class NumberSeventeenException(BaseException):
    ...


try:
    n: int = int(input('Введите число: '))
    if n == 17:
        raise NumberSeventeenException ('это 17')

    isinstance(n, int)
    for i in range(n):
        try:
            divide(random.randint(0, 9), random.randint(0, 9), )
        except ZeroDivisionError:
            print(f'ой, не дели на ноль!')
except ValueError:
    print('аааааа!')
except NumberSeventeenException:
    print('ААААА 17!')

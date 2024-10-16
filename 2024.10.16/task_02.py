"""
Задача 2024.10.16.02

Написать функцию для генерации строки из n строчных и заглавных латинских букв
Заглавные должны добавляться в строку только если параметр use_uppercase в функции равен True.
А если параметр use_uppercase не указан при использовании функции, то генерируем строку только из строчных букв.
"""
import random
import string


def generate_string(n, use_uppercase=False):
    if use_uppercase:
        letters = string.ascii_lowercase + string.ascii_uppercase
    else:
        letters = string.ascii_lowercase

    return ''.join(random.choice(letters) for _ in range(n))


print(generate_string(10))
print(generate_string(10, use_uppercase=True))

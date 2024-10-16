"""
Задача 2024.10.16.01

Написать функцию для генерации строки из n строчных латинских букв
"""
import random
import string


def generate_random_string(n):
    if n <= 0:
        return ""
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(n))


n = 100
random_string = generate_random_string(n)
print(random_string)

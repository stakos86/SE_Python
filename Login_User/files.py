"""
Module to store all the functions that help login the user
"""
import os

FILENAME = 'users.txt'


def read_file(filename: str) -> list[str]:
    """
    Function to read the file with users data
    :param filename: string representation of the name of the file to read
    :return: list of strings stored in the file with users data
    """
    # проверки существования файла по заданному пути и возврата пустого списка,
    # если файл не существует.
    if not os.path.exists(filename):
        return []  # возвращает пустой список
    # чтение файла
    with open(filename, 'r', encoding='utf-8') as file:
        return [line.strip() for line in file.readlines()]  # возвращает после прочтения списка


def write_file(filename: str, data: list[str]) -> None:
    with open(filename, 'w', encoding='utf-8') as file:
        for line in data:
            file.write(line + '\n')


if __name__ == '__main__':
    read_file(FILENAME)


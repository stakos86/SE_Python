import os


def read_tasks_file(filename) -> list[str]:
    if not os.path.exists(filename):
        return []
    with open(filename, 'r', encoding='utf-8') as file:
        return [task.strip() for task in file.readlines()]


def save_tasks_file(filename, list_of_tasks) -> None:
    with open(filename, 'w', encoding='utf-8') as file:
        file.write('\n'.join(list_of_tasks))
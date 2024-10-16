from files import read_tasks_file, save_tasks_file
from tasks import tasks_process
from date_parser import is_date_by_format

FILENAME = "tasks.txt"

def main() -> None:
    """
    Main function
    :return: nothing
    """
    # Объявляем список задач
    tasks = read_tasks_file(FILENAME)
    # Главный цикл
    try:
        tasks_process(tasks)
        is_date_by_format(date)
    finally:
        save_tasks_file(FILENAME, tasks)


if __name__ == '__main__':
    main()
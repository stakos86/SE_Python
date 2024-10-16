def tasks_process(tasks):
    while True:
        # Выводим меню
        print("\n1. Добавить задачу")
        print("2. Удалить задачу")
        print("3. Вывести список всех задач")
        print("4. Выход")
        # Получаем выбор пользователя
        choice: str = input("Введите ваш выбор: ")

        # Проверяем введённые данные
        if choice == '4':
            print("Завершаем работу")
            break
        elif choice == '1':
            add_task_to_list(tasks)
        elif choice == '3':
            print_list(tasks)
        elif choice == '2':
            delete_task_from_list(tasks)
        else:
            print("Вы ввели что-то не то. Ещё разок.")


def print_list(list_to_print: list[str]) -> None:
    """
    Function to print out the list of tasks
    :param list_to_print: list of tasks to print
    :return: Nothing
    """
    if list_to_print:
        for i, item in enumerate(list_to_print):
            task, date = item.split(':')
            print(f"[{i}]: Задача: {task} | Срок: {date}")
    else:
        print("Список задач пуст")


def delete_task_from_list(list_of_tasks: list[str]) -> None:
    """
    Delete task from list of tasks
    :param list_of_tasks: list of tasks to delete from
    :return: Nothing
    """
    # Проверяем если список задач пуст
    if not list_of_tasks:
        print("Список задач пуст")
        return
    #
    index = input("Введите номер задачи: ")
    # Проверяем является ли индекс вообще числом
    if not index.isalnum():
        print("Ошибка | Нужно было ввести целое число")
        return
    # Превращаем str в Int
    index = int(index)
    # Проверяем попадает ли индекс в диапазон количества элементов
    if not 0 <= index < len(list_of_tasks):
        print("Ошибка | Вы ввели неправильное число")
        return
    list_of_tasks.remove(list_of_tasks[index])


def add_task_to_list(list_of_tasks: list[str]) -> None:
    """
    Add task to list of tasks
    :param list_of_tasks: list of tasks to add a task to
    :return: Nothing
    """
    task = input("Введите описание задачи: ")
    date = input("Введите срок задачи: ")
    list_of_tasks.append(f"{task}:{date}")
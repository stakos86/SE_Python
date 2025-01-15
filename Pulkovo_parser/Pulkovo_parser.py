import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook
from openpyxl import load_workbook


def get_and_save_data():
    url = "https://pulkovoairport.ru/passengers/arrival/?when=-1"

    # Получаем данные с сайта
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Ищем первую таблицу на странице (без указания конкретного класса)
    table = soup.find('table')

    if table is None:
        print("Таблица не найдена на странице")
        return None

    # Остальной код остается без изменений...


def run_process():
    result = get_and_save_data()
    if result is not None:
        print(f"Статус рейса FV 6346: {result}")
    else:
        print("Рейс FV 6346 не найден.")


if __name__ == "__main__":
    while True:
        user_input = input("Введите 'run' для выполнения запроса или 'exit' для выхода: ").lower()

        if user_input == 'run':
            run_process()
        elif user_input == 'exit':
            break
        else:
            print("Неверная команда. Попробуйте снова.")

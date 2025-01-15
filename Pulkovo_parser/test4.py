import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PIL import Image
import pytesseract
import os
from datetime import datetime

def get_flight_status():
    # Настройка пути к chromedriver (измените путь, если необходимо)
    chrome_driver_path = "/usr/local/bin/chromedriver"  # Укажите правильный путь
    os.environ["PATH"] += f":{chrome_driver_path}"

    # Настройка пути к tesseract (используем переменную окружения)
    tesseract_path = "/usr/local/bin/tesseract"

    # Настройка драйвера WebDriver
    driver = webdriver.Chrome()

    try:
        # Открытие страницы
        url = "https://pulkovoairport.ru/passengers/arrival/?when=-1"
        driver.get(url)

        # Найдем элемент <body>
        body = driver.find_element(By.TAG_NAME, 'body')

        # Получим высоту документа
        document_height = int(driver.execute_script("return document.body.scrollHeight"))

        # Установим размер окна браузера равным высоте документа
        driver.set_window_size(1920, document_height)

        # Создание скриншота всей страницы
        driver.save_screenshot('screenshot.png')

        # Распознавание текста на скриншоте с указанием языка русский
        text = pytesseract.image_to_string(
            Image.open('screenshot.png'),
            lang='rus',  # Указываем язык русский
            config=f'--oem 3 --psm 6'
        )

        # Формирование имени файла даты и времени
        current_time = datetime.now().strftime("%Y.%m.%d.%H.%M")
        file_name = f"recognized_text_{current_time}.txt"

        # Сохранение распознанного текста в файл
        with open(file_name, "w", encoding="utf-8") as f:
            f.write(text)

        # Чтение содержимого файла и поиск нужной информации
        with open(file_name, "r", encoding="utf-8") as f:
            content = f.read()

        # Поиск значения "FV 6346" и статуса в тексте
        flight_number = "FV 6134"
        status_line = None
        for line in content.split('\n'):
            if flight_number in line:
                status_line = line.strip()
                break

        return status_line

    except Exception as e:
        print(f"Произошла ошибка: {e}")

    finally:
        # Закрытие драйвера
        driver.quit()

    return None

if __name__ == "__main__":
    result = get_flight_status()
    if result:
        print(f"Статус рейса FV 6346: {result}")
    else:
        print("Рейс FV 6346 не найден.")

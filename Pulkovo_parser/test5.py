from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from PIL import Image
import os
from datetime import datetime

def scrape_pulkovo_arrivals():
    # Настройка опций Chrome
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Запуск в безголовом режиме
    chrome_options.add_argument("--disable-gpu")  # Для некоторых систем

    # Настройка пути к chromedriver (измените путь, если необходимо)
    chrome_driver_path = "/usr/local/bin/chromedriver"
    os.environ["PATH"] += f":{chrome_driver_path}"

    # Настройка драйвера WebDriver
    driver = webdriver.Chrome(options=chrome_options)

    try:
        # Открытие страницы
        url = "https://pulkovoairport.ru/passengers/arrival/?when=-1"
        driver.get(url)

        # Даем время для загрузки страницы
        time.sleep(5)  # Увеличьте это значение, если страница загружается медленно

        # Создание скриншота всей страницы
        driver.save_screenshot('screenshot.png')

        print("Скриншот сохранен как screenshot.png")

    except Exception as e:
        print(f"Произошла ошибка: {e}")

    finally:
        # Закрытие драйвера
        driver.quit()

if __name__ == "__main__":
    scrape_pulkovo_arrivals()

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PIL import Image
import pytesseract


def get_flight_status():
    # Настройка драйвера WebDriver (подключите chromedriver)
    driver = webdriver.Chrome()

    try:
        # Открытие страницы
        url = "https://pulkovoairport.ru/passengers/arrival/?when=-1"
        driver.get(url)

        # Ожидание загрузки таблицы с рейсами
        table = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "table.flight-table"))
        )

        # Создание скриншота таблицы
        table.screenshot('table_screenshot.png')

        # Вырезание области таблицы
        location = table.location
        size = table.size

        # Создание объекта Image из скриншота
        screenshot = Image.open('table_screenshot.png')

        # Вырезание области таблицы
        left = location['x']
        top = location['y'] + size['height']
        right = location['x'] + size['width']
        bottom = location['y'] + 2 * size['height']
        img = screenshot.crop((left, top, right, bottom))

        # Сохранение вырезанной области
        img.save('table_area.png')

        # Создание скриншота всей страницы
        driver.save_screenshot('full_page_screenshot.png')

        # Распознавание текста на скриншоте всей страницы
        full_text = pytesseract.image_to_string(Image.open('full_page_screenshot.png'))

        # Поиск нужной информации в распознанном тексте
        flight_status = None
        for line in full_text.split('\n'):
            if "FV 6346" in line:
                flight_status = line.strip()
                break

        return flight_status

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

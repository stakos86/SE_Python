import requests
from bs4 import BeautifulSoup

url = "https://pulkovoairport.ru/passengers/arrival/?when=-1"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Проверьте наличие таблицы
tables = soup.find_all('table')
print(f"Найдено таблиц: {len(tables)}")

# Выведите первые несколько таблиц для проверки
for i, table in enumerate(tables[:5], 1):
    print(f"Таблица {i}:")
    print(table)

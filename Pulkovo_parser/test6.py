import requests
from bs4 import BeautifulSoup

url = "https://pikabu.ru/story/novinki_kino_poyavivshiesya_v_seti_na_14122024_12135755"
response = requests.get(url)
html_content = response.text

soup = BeautifulSoup(html_content, 'html.parser')

target_value = "Fremont"
for element in soup.find_all('td'):
    if target_value in element.text:
        print(f"Значение '{target_value}' найдено в ячейке:")
        print(element)
        break
else:
    print(f"Значение '{target_value}' не найдено на странице")

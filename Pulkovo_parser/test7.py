import requests
from bs4 import BeautifulSoup

url = "https://pikabu.ru/story/novinki_kino_poyavivshiesya_v_seti_na_14122024_12135755"
response = requests.get(url)
html_content = response.text

soup = BeautifulSoup(html_content, 'html.parser')

target_word = "Гладиатор"

# Поиск первого вхождения слова
first_occurrence = None
for element in soup.find_all(text=True):
    if target_word in element:
        first_occurrence = element
        break

if first_occurrence:
    # Найдем индекс слова в тексте элемента
    index = first_occurrence.find(target_word)

    # Выведем слово и следующие 20 символов
    print(f"Слово '{target_word}' найдено:")
    print(first_occurrence[index:index + len(target_word) + 20])
else:
    print(f"Слово '{target_word}' не найдено на странице.")

import requests
from bs4 import BeautifulSoup

def get_most_common_word(html_content, tag):
    soup = BeautifulSoup(html_content, 'html.parser')
    elements = soup.find_all(tag)

    words = []
    for element in elements:
        words.extend(element.get_text().split())

    if not words:
        return None

    most_common_word = max(set(words), key=words.count)
    return most_common_word

url = input("Podaj adres strony internetowej: ")
tag = input("Wybierz znacznik do analizy (np. <h1>, <h2>, <p>, <ol>): ")

response = requests.get(url)
if response.status_code == 200:
    most_common_word = get_most_common_word(response.content, tag)
    if most_common_word:
        print("Najczęściej występujące słowo wewnątrz {}: {}".format(tag, most_common_word))
    else:
        print("Brak tekstu wewnątrz znacznika {} na stronie.".format(tag))
else:
    print("Nie udało się pobrać zawartości strony.")
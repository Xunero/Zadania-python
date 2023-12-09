import requests
from bs4 import BeautifulSoup
import tkinter as tk
from tkinter import messagebox

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

def analyze_website(url, tag):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Sprawdzenie czy zapytanie zakończone sukcesem

        most_common_word = get_most_common_word(response.content, tag)
        if most_common_word:
            return most_common_word
        else:
            return "Brak tekstu wewnątrz znacznika {} na stronie.".format(tag)
    except requests.exceptions.HTTPError as errh:
        return "Błąd HTTP: {}".format(errh)
    except requests.exceptions.ConnectionError as errc:
        return "Błąd połączenia: {}".format(errc)
    except requests.exceptions.Timeout as errt:
        return "Błąd timeout: {}".format(errt)
    except requests.exceptions.RequestException as err:
        return "Nieznany błąd: {}".format(err)

def analyze_links(url, tag):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Sprawdzenie czy zapytanie zakończone sukcesem

        soup = BeautifulSoup(response.content, 'html.parser')
        links = soup.find_all('a', href=True)

        results = []
        for link in links:
            link_url = link['href']
            link_result = analyze_website(link_url, tag)
            results.append((link_url, link_result))

        return results
    except requests.exceptions.HTTPError as errh:
        return [("Błąd HTTP:", errh)]
    except requests.exceptions.ConnectionError as errc:
        return [("Błąd połączenia:", errc)]
    except requests.exceptions.Timeout as errt:
        return [("Błąd timeout:", errt)]
    except requests.exceptions.RequestException as err:
        return [("Nieznany błąd:", err)]

def on_analyze_button_click():
    url = entry_url.get()
    tag = entry_tag.get()

    if not url or not tag:
        messagebox.showerror("Błąd", "Wprowadź poprawne dane.")
        return

    link_results = analyze_links(url, tag)

    if link_results:
        result_text.set("\n".join(["{}: {}".format(link, result) for link, result in link_results]))
    else:
        result_text.set("Błąd analizy stron.")

# Tworzenie GUI
root = tk.Tk()
root.title("Analiza Strony Internetowej")

# Widgety
label_url = tk.Label(root, text="Adres Strony:")
entry_url = tk.Entry(root, width=50)
label_tag = tk.Label(root, text="Znacznik do Analizy (np. <h1>, <h2>, <p>, <ol>):")
entry_tag = tk.Entry(root, width=20)
analyze_button = tk.Button(root, text="Analizuj", command=on_analyze_button_click)
result_text = tk.StringVar()
result_label = tk.Label(root, textvariable=result_text, wraplength=400, justify=tk.LEFT)

# Rozmieszczenie widgetów
label_url.pack(pady=5)
entry_url.pack(pady=5)
label_tag.pack(pady=5)
entry_tag.pack(pady=5)
analyze_button.pack(pady=10)
result_label.pack(pady=10)

# Uruchomienie głównej pętli GUI
root.mainloop()
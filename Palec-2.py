import csv
import time

def wczytaj_tabele(nazwa_pliku, delimiter=';'):
    try:
        with open(nazwa_pliku, 'r', encoding='utf-8-sig') as plik_csv:
            czytnik = csv.DictReader(plik_csv, delimiter=delimiter)
            tabela = [row for row in czytnik]
    except FileNotFoundError:
        print(f"File '{nazwa_pliku}' not found.")
        return [], []

    naglowki = czytnik.fieldnames
    print("Naglowki:", naglowki)
    print("Tabela:", tabela)
    return naglowki, tabela

def wyszukaj_prosta_metoda(tabela, kolumna_do_szukania, szukane):
    wyniki = []
    for wiersz in tabela:
        if szukane.lower() == str(wiersz[kolumna_do_szukania]).lower():
            wyniki.append(wiersz)
    return wyniki

def main():
    nazwa_pliku = 'dane.csv'  # Zmień na nazwę swojego pliku CSV
    naglowki, tabela = wczytaj_tabele(nazwa_pliku)

    if not naglowki or not tabela:
        return  # Wyjdź, jeśli plik nie został znaleziony

    print("Dostępne kolumny:")
    print(naglowki)

    kolumna_do_szukania = input("Podaj nazwę kolumny, po której chcesz wyszukać: ")
    szukane = input("Podaj wartość do wyszukania: ")

    if kolumna_do_szukania not in naglowki:
        print("Podana kolumna nie istnieje.")
        return
    start = time.time()

    wyniki = wyszukaj_prosta_metoda(tabela, kolumna_do_szukania, szukane)

    time.sleep(5)
    stop = time.time()    

    print(f"Wyszukiwanie trwalo: {stop - start}")
    if not wyniki:
        print("Brak wyników.")
    else:
        print(f"Wyniki wyszukiwania w kolumnie {kolumna_do_szukania}:")
        for wynik in wyniki:
            print(wynik)

if __name__ == "__main__":
    main()
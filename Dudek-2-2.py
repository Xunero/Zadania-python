import random
import csv

# Funkcja do losowania danych osobowych
def losuj_dane(imiona, nazwiska, ulice, miasta, kraje):
    imie = random.choice(imiona)
    nazwisko = random.choice(nazwiska)
    pesel = ''.join(random.choices("0123456789", k=11))
    ulica = random.choice(ulice)
    nr_domu = str(random.randint(1, 50))
    miasto = random.choice(miasta)
    kraj = random.choice(kraje)
    return [imie, nazwisko, pesel, ulica, nr_domu, miasto, kraj]

# Funkcja do zapisywania danych do pliku CSV
def zapisz_do_pliku(plik, dane):
    with open(plik, 'a', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=';')
        writer.writerow(dane)

# Wczytaj dostępne dane z plików
with open('imiona.txt') as f:
    imiona = f.read().splitlines()
with open('nazwiska.txt') as f:
    nazwiska = f.read().splitlines()
with open('ulice.txt') as f:
    ulice = f.read().splitlines()
with open('miasta.txt', encoding='utf-8') as f:
    miasta = f.read().splitlines()
with open('kraje.txt') as f:
    kraje = f.read().splitlines()

# Pobierz liczbę danych do wygenerowania od użytkownika
liczba_danych = int(input("Podaj liczbę danych do wygenerowania: "))

# Wygeneruj i zapisz dane
for _ in range(liczba_danych):
    dane = losuj_dane(imiona, nazwiska, ulice, miasta, kraje)
    zapisz_do_pliku('dane_osobowe.csv', dane)

print(f"Zapisano {liczba_danych} losowych danych osobowych do pliku 'dane_osobowe.csv'.")

choose = input(print("Chcesz wczytac dane z pliku? (t/n)"))

if choose == t:
    wypisz = input("Podaj wartosc do wyszukania w pliku: ")
    with open('dane_osobowe.csv', 'r') as dane:
       reader = csv.reader(dane,delimiter=",")
       for data in dane:
          if wypisz in data:
               print(data)
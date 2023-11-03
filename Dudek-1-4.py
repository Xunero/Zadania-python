# Funkcja do policzenia ilości liter, liter bez spacji i liter bez podanego znaku
def policz_litery(zdanie, znak):
    ilosc_liter = len(zdanie)
    ilosc_liter_bez_spacji = len(zdanie.replace(" ", ""))
    ilosc_liter_bez_znaku = len(zdanie.replace(znak, ""))
    return ilosc_liter, ilosc_liter_bez_spacji, ilosc_liter_bez_znaku

# Funkcja do wypisania wszystkich wyrazów w zdaniu
def wypisz_wyrazy(zdanie):
    wyrazy = zdanie.split()
    for wyraz in wyrazy:
        print(wyraz)

# Funkcja do podziału zdania na podstawie podanego znaku i umieszczenia wyniku w liście
def podziel_i_zapisz(zdanie, znak):
    lista_napisow = zdanie.split(znak)
    return lista_napisow

# Pobieranie zdania od użytkownika
zdanie = input("Podaj zdanie: ")
znak = input("Podaj znak, przez który chcesz podzielić zdanie: ")

# Wywołanie funkcji i wyświetlenie wyników
ilosc_liter, ilosc_liter_bez_spacji, ilosc_liter_bez_znaku = policz_litery(zdanie, znak)
print(f"Ilość liter w zdaniu: {ilosc_liter}")
print(f"Ilość liter bez spacji: {ilosc_liter_bez_spacji}")
print(f"Ilość liter bez znaku '{znak}': {ilosc_liter_bez_znaku}")

print("Zdanie podzielone przez spacje: ")
wypisz_wyrazy(zdanie)

lista_napisow = podziel_i_zapisz(zdanie, znak)
print(f"Zdanie podzielone przez znak '{znak}':")
print(lista_napisow)
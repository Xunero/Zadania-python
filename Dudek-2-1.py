def znajdz_min_max_pozycje(lista):
    if len(lista) == 0:
        return None, None, None, None
    min_wartosc = lista[0]
    max_wartosc = lista[0]
    min_pozycja = 0
    max_pozycja = 0

    for i, liczba in enumerate(lista):
        if liczba < min_wartosc:
            min_wartosc = liczba
            min_pozycja = i
        if liczba > max_wartosc:
            max_wartosc = liczba
            max_pozycja = i

    return min_wartosc, max_wartosc, min_pozycja, max_pozycja

def mediana(lista):
    
    if len(lista) % 2 == 0:
      niepa = len(lista) / 2
      parzy = int(niepa)
      parzy = niepa + 1
      x = lista[niepa] 
      y = lista[parzy]
      median = (x + y)
      return median
    
    if len(lista) % 2 == 1:
        niepa = len(lista) / 2
        xxx = int(niepa)
        miedin = lista[xxx]
        return miedin



def srednia(lista):
    if len(lista) == 0:
        return None
    suma = sum(lista)
    srednia_wartosc = suma / len(lista)
    return srednia_wartosc

def znajdz_pozycje_wartosci(lista, wartosc):
    if wartosc in lista:
        pozycja = lista.index(wartosc)
        return pozycja
    else:
        return None
    
lista_liczb = []
while len(lista_liczb) < 15:
    liczba = int(input(f"Podaj {len(lista_liczb) + 1}. liczbę całkowitą: "))
    if liczba not in lista_liczb:
        lista_liczb.append(liczba)
    else:
        print("Podana liczba już znajduje się na liście. Podaj inną liczbę.")

min_wartosc, max_wartosc, min_pozycja, max_pozycja = znajdz_min_max_pozycje(lista_liczb)
srednia_wartosc = srednia(lista_liczb)
med = mediana(lista_liczb)

print(f"Najmniejsza wartość: {min_wartosc}, pozycja: {min_pozycja}")
print(f"Największa wartość: {max_wartosc}, pozycja: {max_pozycja}")
print(f"Średnia wartość: {srednia_wartosc}")
print(f"Mediana: {med} ")

wartosc_uzytkownika = int(input("Podaj wartość, której pozycję chcesz znaleźć: "))
pozycja_wartosci = znajdz_pozycje_wartosci(lista_liczb, wartosc_uzytkownika)

if pozycja_wartosci is not None:
    print(f"Pozycja wartości {wartosc_uzytkownika} w liście: {pozycja_wartosci}")
else:
    print(f"Wartość {wartosc_uzytkownika} nie występuje w liście.")

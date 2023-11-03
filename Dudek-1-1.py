import math

# Funkcja do obliczania objętości kuli
def oblicz_objetosc_kuli(promien):
    return (4/3) * 3.14 * promien**3

# Funkcja do obliczania pola powierzchni kuli
def oblicz_pole_powierzchni_kuli(promien):
    return 4 * 3.14 * promien**2

# Funkcja do obliczania objętości prostopadłościanu
def oblicz_objetosc_prostopadloscianu(a, b, c):
    return a * b * c

# Funkcja do obliczania pola powierzchni prostopadloscianu
def oblicz_pole_powierzchni_prostopadloscianu(a, b, c):
    return 2 * (a * b + b * c + a * c)

# Funkcja do obliczania objętości stożka
def oblicz_objetosc_stozka(r, h):
    return (1/3) * 3.14 * r**2 * h

# Funkcja do obliczania pola powierzchni stożka
def oblicz_pole_powierzchni_stozka(r, l):
    return 3.14 * r * (r + l)

# Główna funkcja programu
def main():
    print("Wybierz bryłę do obliczeń:")
    print("a) Kula")
    print("b) Prostopadłościan")
    print("c) Stożek")
    wybor = input("Twój wybór: ")

    if wybor == 'a':
        promien = float(input("Podaj promień kuli: "))
        objetosc = oblicz_objetosc_kuli(promien)
        pole_powierzchni = oblicz_pole_powierzchni_kuli(promien)
    elif wybor == 'b':
        a = float(input("Podaj długość boku a: "))
        b = float(input("Podaj długość boku b: "))
        c = float(input("Podaj długość boku c: "))
        objetosc = oblicz_objetosc_prostopadloscianu(a, b, c)
        pole_powierzchni = oblicz_pole_powierzchni_prostopadloscianu(a, b, c)
    elif wybor == 'c':
        r = float(input("Podaj promień podstawy stożka: "))
        h = float(input("Podaj wysokość stożka: "))
        objetosc = oblicz_objetosc_stozka(r, h)
        l = math.sqrt(r**2 + h**2)  # obliczamy długość tworzącej
        pole_powierzchni = oblicz_pole_powierzchni_stozka(r, l)
    else:
        print("Nieprawidłowy wybór bryły.")
        return

    print(f"Objętość wybranej bryły: {objetosc}")
    print(f"Pole powierzchni wybranej bryły: {pole_powierzchni}")


main()
import random
import pickle

class Pole:
    def __init__(self, nazwa, cena):
        self.nazwa = nazwa
        self.cena = cena
        self.wlasciciel = None

    def kup(self, gracz):
        self.wlasciciel = gracz

    def __str__(self):
        return f"{self.nazwa} - Cena: {self.cena} - Właściciel: {self.wlasciciel}"

class Miasto(Pole):
    def __init__(self, nazwa, cena, stawka):
        super().__init__(nazwa, cena)
        self.stawka = stawka

    def pobierz_oplatę(self):
        return self.stawka

class Kostka:
    def rzut(self):
        return random.randint(1, 6)

class Gracz:
    def __init__(self, imie):
        self.imie = imie
        self.pieniadze = 1000
        self.pola = []

    def zaplac(self, kwota, inny_gracz):
        self.pieniadze -= kwota
        inny_gracz.pieniadze += kwota

    def kup_pole(self, pole):
        if pole.nazwa == "Start":
            print("Nie można kupić pola Start.")
            return False

        if pole.wlasciciel is None and self.pieniadze >= pole.cena:
            pole.kup(self)
            self.pola.append(pole)
            self.pieniadze -= pole.cena
            return True
        else:
            return False

    def __str__(self):
        return f"Gracz: {self.imie} \n- Pieniądze: {self.pieniadze} \n- Posiadane pola: {', '.join([pole.nazwa for pole in self.pola])}"

class Plansza:
    def __init__(self):
        self.pola = [
            Pole("Start", 0),
            Miasto("Warszawa", 100, 20),
            Miasto("Krakow", 150, 25),
            Miasto("Gdansk", 200, 30),
            Miasto("Poznan", 180, 28),
            Miasto("Wroclaw", 160, 22),
            Pole("Szczecin", 120),
            Pole("Lodz", 140),
            Pole("Katowice", 170),
            Pole("Bialystok", 130),
            Pole("Rzeszow", 190)
        ]

    def wyswietl(self, pozycja):
        print("Aktualna plansza:")
        for i, pole in enumerate(self.pola):
            if i == pozycja:
                print(f"[{i}] {pole} <-- Aktualna pozycja gracza")
            else:
                print(f"[{i}] {pole}")

class Gra:
    def __init__(self):
        self.plansza = Plansza()
        self.gracze = [Gracz("Gracz1"), Gracz("Gracz2")]
        self.kostka = Kostka()

    def rozpocznij(self):
        kolejka = 0
        while True:
            gracz = self.gracze[kolejka % len(self.gracze)]
            print("\n", "=" * 30)
            print(f"Ruch gracza {gracz.imie}")
            self.plansza.wyswietl(self.plansza.pola.index(gracz.pola[-1]) if gracz.pola else 0)

            opcja = input("Co chcesz zrobić? (rzut - rzut kostką, r - zapisz rozgrywkę, q - zakończ): ")

            if opcja == 'rzut':
                wynik_rzutu = self.kostka.rzut()
                print(f"{gracz.imie} rzuca kostką i wyrzuca: {wynik_rzutu}")

                if not gracz.pola:  # Jeśli gracz nie posiada jeszcze żadnych pól
                    nowa_pozycja = 1  # Zaczynamy od pierwszego pola
                else:
                    nowa_pozycja = (self.plansza.pola.index(gracz.pola[-1]) + wynik_rzutu) % len(self.plansza.pola)
                    gracz.pola.append(self.plansza.pola[nowa_pozycja])
                    print(f"{gracz.imie} przesuwa się na pole {self.plansza.pola[nowa_pozycja].nazwa}")

                opc = input("Jesli chcesz kupic pole wpisz k: ")
                if opc == 'k':
                    pole_do_kupienia = self.plansza.pola[nowa_pozycja]
                    if gracz.kup_pole(pole_do_kupienia):
                        print(f"{gracz.imie} kupił pole {pole_do_kupienia.nazwa}")
                        oplata = pole_do_kupienia.pobierz_oplatę()
                        gracz.zaplac(oplata, pole_do_kupienia.wlasciciel)
                        print(f"{gracz.imie} zapłacił {oplata} graczowi {pole_do_kupienia.wlasciciel.imie}")
                        kolejka += 1

            elif opcja == 'r':
                self.zapisz_gre()
            elif opcja == 'q':
                break

    def zapisz_gre(self):
        nazwa_pliku = input("Podaj nazwę pliku do zapisu: ")
        with open(nazwa_pliku, 'wb') as plik:
            pickle.dump(self, plik)
        print(f"Stan gry zapisany do pliku {nazwa_pliku}")

if __name__ == "__main__":
    gra = Gra()
    gra.rozpocznij()
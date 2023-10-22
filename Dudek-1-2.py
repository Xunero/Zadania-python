oceny = {}  # Słownik do przechowywania ocen

while True:
    print("Co chcesz zrobić?")
    print("1. Wprowadź ocenę z przedmiotu")
    print("2. Oblicz średnią ze wszystkich ocen")
    print("3. Oblicz średnią dla wybranego przedmiotu")
    print("4. Zakończ program")
    
    wybor = input("Twój wybór: ")
    
    if wybor == '1':
        przedmiot = input("Podaj nazwę przedmiotu: ")
        ocena = float(input("Podaj ocenę: "))
        
        if przedmiot in oceny:
            oceny[przedmiot].append(ocena)
        else:
            oceny[przedmiot] = [ocena]
        
        print("Ocena dodana.")
    
    elif wybor == '2':
        if not oceny:
            print("Brak ocen do obliczenia średniej.")
        else:
            srednia = sum(ocena for oceny_w_przedmiocie in oceny.values() for ocena in oceny_w_przedmiocie) / sum(len(oceny_w_przedmiocie) for oceny_w_przedmiocie in oceny.values())
            print(f"Średnia ze wszystkich ocen: {srednia:.2f}")
    
    elif wybor == '3':
        przedmiot = input("Podaj nazwę przedmiotu, dla którego chcesz obliczyć średnią: ")
        
        if przedmiot in oceny:
            srednia = sum(ocena for ocena in oceny[przedmiot]) / len(oceny[przedmiot])
            print(f"Średnia dla przedmiotu '{przedmiot}': {srednia:.2f}")
        else:
            print("Brak ocen dla wybranego przedmiotu.")
    
    elif wybor == '4':
        break
    
    else:
        print("Nieprawidłowy wybór. Wybierz 1, 2, 3 lub 4.")

        
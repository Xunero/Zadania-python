import random 
import time
import sys

# Tworzenie tablicy z 50 miejscami i wypełnienie jej losowymi liczbami
def tablicalos(dlug):
    return [random.randint(1, 1000) for _ in range(dlug)]
    

# Funkcja sortująca szybka
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

rozmiar = int(input("Podaj rozmiar tabliczy: "))

tryb = input("Chcesz sam wpisac wartosci ? wpisz M. Chcesz losowe wartosci? wpisz L: ")

array = []

if tryb == "L":
    array = tablicalos(rozmiar)
elif tryb == "M":
    for i in range(rozmiar):
        liczba = float(input("Podaj liczbę: "))
        array.append(liczba)
else:
    print("Wprowadziles zla wartosc")
    sys.exit()

# Sortowanie tablicy
start = time.time()

sorted_array = quick_sort(array)
time.sleep(5) #opoznienie aby pokazac ze timer dziala
stop = time.time()



# Wyświetlenie oryginalnej tablicy
print("Oryginalna tablica:")
print(array)

# Wyświetlenie posortowanej tablicy
print("Posortowana tablica:")
print(sorted_array)

print(f"Sortowanie trwalo: {stop - start}" )

def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid  # Znaleziono liczbę, zwracamy jej indeks
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1  # Liczba nie została znaleziona

# Przykładowa tablica (musi być posortowana)



target_number = int(input("Podaj Liczbe do znalezienia: "))

# Wywołujemy funkcję wyszukiwania binarnego
start = time.time()

result = binary_search(sorted_array, target_number)

time.sleep(5)
stop = time.time()
print(f"Wyszukiwanie trwalo: {stop - start}")



if result != -1:
    print(f'Liczba {target_number} została znaleziona na indeksie {result}.')
else:
    print(f'Liczba {target_number} nie została znaleziona w tablicy.')
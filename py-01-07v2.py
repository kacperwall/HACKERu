"""
stworzy pusta liste. Popros uzytkownika o informacje ile produktow chce wprowadzic
w petli popros uzytkownika o wprowadzenie produktu i jego ceny
Cene wprowadzonych produktow wyswietlamy na zakonczenie programu
"""

produkty = {}

suma = 0

while True:
    nazwa = input("podaj nazwe produktu albo wpisz koniec: ").strip().lower()

    if nazwa == "koniec":
        break

    cena = float(input("podaj cene produktu"))
    produkty[nazwa] = cena
    suma += cena # to samo co suma = suma + cena

print("suma produktow:", suma)

while True:
    odpowiedz = input("Czy wyswietlic wprowadzone wartosci? ") # "Tak" "TAK"
    if odpowiedz.upper().strip() == "TAK":
        print(produkty)
        print("suma produktow:", suma)
        breakWawrzyniak
    elif odpowiedz.upper().strip() == "NIE":
        print("bye bye")
        break
    else :
        print("bledna odpoweidz. Oczekuje Tak lub Nie! Sprobuj ponownie !!!")
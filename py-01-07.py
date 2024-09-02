"""
stworzy pusta liste. Popros uzytkownika o informacje ile produktow chce wprowadzic
w petli popros uzytkownika o wprowadzenie produktu i jego ceny
Cene wprowadzonych produktow wyswietlamy na zakonczenie programu
"""

produkty = {}

ile_produktow = int(input("Podaj ilosc produktow do wprowadzenia"))
suma = 0

for x in range(ile_produktow):
    nazwa = input("podaj nazwe produktu: ")
    cena = float(input("podaj cene produktu"))
    produkty[nazwa] = cena
    suma += cena # to samo co suma = suma + cena

print("suma produktow:", suma)
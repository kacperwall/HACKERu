"""
Napiz program, ktory pobiera od uzytkownika 2 wartosci numeryczne
Napisz funkcje, ktora mnozy obie wartosci przez 2
funkcja na koniec dodaje obie wartosci do siebie i zwraca rezultat takiego dzialani
Na koniec wyswietlamy rezultat!
"""
#v1
def obliczenia(arg1, arg2):
    arg1 *= 2 # arg1 = arg1 * 2
    arg2 *= 2 # arg2 = arg2 * 2
    return arg1 + arg2

arg1 = int(input("podaj pierwszy parametr: "))
arg2 = int(input("podaj drugi parametr: "))
rezultat = obliczenia(arg1,arg2)
print("rezultat: ",rezultat)
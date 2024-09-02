"""
Napisz program, ktory pobiera od uzytkownika dwie wartosci liczbowe
i probuje je podzielic. Jezeli program napotka blad to wyswetl wlasciwy komunikat
"""
import funkcje_przyklady as f

print('jestem w programie, ktory dzieli dwie liczby calkowite!')
try:

    num1 = f.pobierz_wartosc_numeryczna()
    num2 = f.pobierz_wartosc_numeryczna()
    print(num1 / num2)
except Exception as error:
    print("Mam blad: ", error)

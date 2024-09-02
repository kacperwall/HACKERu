"""
Napisz program, ktory pobiera od uzytkownika 2 wartosci
i sprawdza, ktora jest wieksza
np: uzytkownika wpisuje 20 i 30. Wiec wyswietlamy komunikat, ze '30 jest wieksze'
"""

wartoscpierwsza = float(input("Podaj pierwsza wartość: "))
wartoscdruga = float(input("Podaj druga wartość: "))

if wartoscpierwsza > wartoscdruga:
    print(wartoscpierwsza, "wartość jest większa.")
elif wartoscpierwsza < wartoscdruga:
    print(wartoscdruga, "wartość jest większa.")
else:
    print("Obie wartości są równe.")
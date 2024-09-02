# funcka dodajaca -ish na koniec tekstu wprowadzonego od uzytkownika:

def dodaj_ish(tekst):
    return tekst+'-ish'

while True:
    od_uzytkownika = input("Podaj teskt lub wpisz EXIT")
    if od_uzytkownika == 'EXIT':
        break
    else :
        print( dodaj_ish(od_uzytkownika) )
'''Napisz program, ktory pobiera od uzytkownika wiek i sprawdza czy uzytkownika jest pelnoletni
Jezeli wiek >= 18 to wyswietlamy 'dzien dobry Pani/Panu'
jezeli wiek < 18 to wyseitlamy 'czesc mlody'''

wiek = int(input("Podaj swój prawdziwy wiek: "))
if wiek >= 18:
    print("Dzien dobry Pani/Panu")
else:
    print("Czesc mlody.")

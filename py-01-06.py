"""
Wprowadz 4 marki samochodu
zapytaj uzytkownika, czy wyswietlic wprowadzone wartosci
jezeli Tak, to wyswietl zawartosc listy
jezeli NIE, to wyjdz z programu wyswietlajac komunikat 'bye bye'
"""


pojazdy = []

for x in range(4):
    nazwa = input("Podaj marke samochodu: ")
    pojazdy.append(nazwa)

while True:
    odpowiedz = input("Czy wyswietlic wprowadzone wartosci? ")
    if odpowiedz.lower().strip() == "tak":
        print(pojazdy)
        break
    elif odpowiedz.lower().strip() == "nie":
        print("bye bye")
        break
    else :
        print("bledna odpoweidz. Oczekuje Tak lub Nie! Sprobuj ponownie !!!")





# wykorzystanie funkcji len() w obliczaniu dlugosci listy:
lista = ['opel', 'mazda', 'ford', 'toyota']
print( len(lista) )

for x in range(len(lista)): # range(4)
    print(lista[x])



#lista zagniezdzona:
lista = []

for i in range(4):
    lista.append( [] )
    for j in range(10):
        lista[i].append(j)

print(lista)

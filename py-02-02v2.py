def mnozenie2 (x,y):
    x *= 2
    y *= 2
    print(x+y)
a = int(input("podaj pierwsza liczbe: "))
b = int(input("podaj druga liczbe: "))
mnozenie2(a,b)


#przyklad przekazywania listy do funkcji:
def ListPassing( list ):
    for name in list:
        name = name + " is available "
        print(name)

names = ["john", 'brad', "coper", "loren"]
ListPassing( "jakis tekst" ) # ten tekst jest przekazywany zamiast listy 'names' i wyswietlane sa literka po literce
print("""
pobierz od uzytkownika 2 wartosci i podaj operacje jaka chcesz na nich wykonac
+,-,*,/. W zaleznosci o wyboru uzytkownika zastuj te operacje na pobranych wartosciach
""")

x = int(input("Podaj pierwsza wartosc: "))
y = int(input("podaj druga wartosc: "))
operator = input("podaj operator (+,-,*,/): ")

if operator == "+":
    print(f" {x} + {y} = { x+y }")
elif operator == "-":
    print(f" {x} - {y} = { x-y }")
elif operator == "*":
    print(f" {x} * {y} = { x*y }")
elif operator == "/":
    print(f" {x} / {y} = { x/y }")
else:
    print("Bledny wybor!")

print("koniec programu")


#przyklad uzycia tupli i listy w kodzie:

tupla1 = ("Warszawa","00-100", 33, 444, True, 0.33)
print( tupla1[0], tupla1[5] )

    #    0          1         2  3     4     5
lista = ["Warszawa","00-100", 33, 444, True, 0.33]
# kod-pocztowy  i poczta
print( f" kod pocztowy: {lista[1]}, poczta: {lista[0]}" )


lista2 = ["Warszawa","00-100", 33, 444, True, 0.33]
print(lista2)
del lista2[1]
print(lista2)

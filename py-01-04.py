#         0      1       2         3
colors = ["RED", "BLUE", "YELLOW", "BROWN", "BLUE"]

colors.insert(2,"COLOR")
colors.append("BLACK")

del colors[0]
colors.remove("BLUE")
colors.pop(3)
print(colors)




#przyklad_slownika:
lista = ['Jakub','Szepielak','Warszawa']
lista.insert(0,"Mr.")

slownik = { "nazwisko":"Szepielak", "miasto":"Warszawa", "imie":"Jakub"}

print("imie:",lista[0],"nazwisko:", lista[1])
print("imie:",slownik["imie"],"nazwisko:", slownik["nazwisko"])

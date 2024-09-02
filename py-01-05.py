"""
Napisz program, ktory pobiera od uzytkownika liczbe
i wyswietla 'hello world' tyle razy ile poprosil go uzytkownik
"""

counter = int(input("podaj liczbe 'Hello World'"))

while counter != 0:
    print("Hello world!")
    counter -= 1
print("I'm out")
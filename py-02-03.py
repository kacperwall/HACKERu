"""
Napisz program, ktory przechowuje wartosci login:haslo w slowniku
napisz funkcje, ktora sprawdza czy kombinacja login i haslo jest w zdefiniowanym slowniku
"""

db = {
    #login #pass
    "kali":"kali",
    "admin":"Aa123456",
    "johnd":"Aa123456",
    "administrator":"admin"
}

def autentykacja(login, haslo):
    for key in db:
        if key == login and db[key] == haslo:
            return True
    return False


login = input("Podaj login: ")
password = input("Podaj haslo: ")

if autentykacja(login, password):
    print("Witamy w systemie")
else:
    print("bledny login lub haslo")
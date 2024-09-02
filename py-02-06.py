"""
Napisz program, ktory pobiera od uzytkownika jakies logi i dodaje do nich znacznik czas
wykorzystaj biblioteke 'datetime' to pobierania bierzacego czasu
"""
import datetime

db = {
    # login #pass
    "kali": "kali",
    "admin": "Aa123456",
    "johnd": "Aa123456",
    "administrator": "admin"
}
log = [

]


def autentykacja(login, haslo):
    for key in db:
        log.append(f"{datetime.datetime.now()} [DEBUG] sprawdzam poprawnosc danych z uzytkownikiem: {key}, {db[key]}")
        if key == login and db[key] == haslo:
            log.append(f"{datetime.datetime.now()} [INFO] odnotowalismy logowanie uzytkownika: {login}")
            return True

    log.append(f"{datetime.datetime.now()} [WARNING] bledne logowanie dla uzytkownika i hasla: {login}, {haslo}")
    return False


while True:
    login = input("Podaj login lub wpisz EXIT zeby wyjsc: ")

    if login.strip().upper() == "EXIT":
        break

    password = input("Podaj haslo: ")

    if autentykacja(login, password):
        print("Witamy w systemie")
    else:
        print("bledny login lub haslo")

for linijka in log:
    print(linijka)
"""
Napisz program, ktory generuje liczbe losowa i prosi uzytkownika od jej odgadniecie
Po odgadnieciu liczby wyswietla uzytkownikowi informacje ile prob potrzebowal, zeby zgadac !
"""
# zdanie: zwieksz zakres liczb i zmien logike algorytmu,
# tak zeby informowac uzykownika jak daleko jest od wylosowanej liczby
# jezeli dalej niz 20 to lodowato
# jezeli miedzy 20 a 10 to zimno
# jezeli w 10 to cieplo
# jezeli w 3 to goraco
import random


wylosowana = random.randint(1,10) #mozna zwiekszyc zakres

counter = 0
while True:
    counter+=1
    odpowiedz = int(input("Podaj liczbe: "))
    if wylosowana == odpowiedz:
        break

print(f"wygrales po {counter} probach")
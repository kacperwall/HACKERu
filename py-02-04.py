"""
Napisz program, ktory pobiera od uzytkownika jakis tekst i zlicza ilosc znakow wystepujacych w tekscie
spacje tez sa liczone.
implemntacje: len("hello world")
"""

counter = 0

def keylogger():
    global counter
    tekst = input("Podaj jakis tekst: ")
    if tekst.strip().upper() == "EXIT":
        return -1
    for c in tekst:
        counter+=1
        # print(c)

while True:
    if keylogger() == -1:
        break

print(counter)

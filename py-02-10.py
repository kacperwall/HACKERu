'''
Napisz program, ktory sprawdza ip twojego komputera.
wykorzystaj biblioteke os
'''

import os

# Wykonanie polecenia systemowego ipconfig i zapisanie wyniku do pliku moje_ip.txt
os.system("ipconfig > moje_ip.txt")

# Otwarcie pliku z wyraźnym określeniem kodowania odpowiedniego dla Windowsa
with open("moje_ip.txt", "r", encoding="cp1252") as plik:
    for linijka in plik:
        if "IPv4" in linijka:
            print(linijka.split()[13])  # Usunięcie niepotrzebnych znaków końca linii

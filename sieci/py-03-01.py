'''wykorzystujac biblioteke urllib3 pobierz kod zrodlowy strony internetowej
i sprawdz status odpowiedzi takiej strony'''

import urllib3
url = "https://hack-yourself-first.com"

http = urllib3.PoolManager()
response = http.request("GET", url)

print(response.status)
print(response.data.decode("UTF-8")) #UTF-8 powoduje, ze strona nie wyswietla sie w jednej linijce, tylko poprawnie interpretuje /r/n

with open("strona.html","w") as plik:
    plik.write(response.data.decode("UTF-8"))
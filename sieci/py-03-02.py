'''wykorzystujac biblioteke request pobierz kod zrodlowy strony internetowej
i sprawdz status odpowiedzi takiej strony'''

import requests

response = requests.get("http://try-hackyourself-first.com")

print(response.status_code)
print(response.text)

with open("strona.html", "w") as plik:
    plik.write(response.data.decode("UTF-8"))
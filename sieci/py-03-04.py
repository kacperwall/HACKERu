'''wykorzystanie biblioteki beatiful soup do parsowania strony
i pobieranie wszystkich pdf-ów na stronie http://scanme.org/'''

import requests
from bs4 import BeautifulSoup

# Adres URL do przeszukania
url = "https://archiwum.mz.gov.pl/zdrowie-i-profilaktyka/grypa/materialy-do-pobrania/"
response = requests.get(url)

# Tworzenie obiektu Beautiful Soup z treści odpowiedzi
soup = BeautifulSoup(response.text, "html.parser")

# Znajdowanie wszystkich linków na stronie
links = soup.find_all('a')

# pobieranie wszystkich pdfów na stronie
for link in links:
    href = link.get('href')
    if href.endswith(".pdf"):
        r = requests.get(href, stream=True)
        with open(href.split("/")[-1], "wb") as plik:
            plik.write(r.content)

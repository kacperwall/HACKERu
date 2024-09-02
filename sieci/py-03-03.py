'''wysyłanie przesyłanie metodą POST wartosci do serwera, w tym przypadku login i haslo'''

import requests

url = "https://hack-yourself-first.com/Account/Login"
dane_logowania = {"Email":"mopob93849@daypey.com", "Password":"aaa"}
response = requests.post(url, dane_logowania)

print(response.status_code)
print(response.text)
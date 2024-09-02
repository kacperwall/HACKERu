credentiale = { "kali": "kali",
"admin": "Aa123456!",
"kowalski": "Jan1234",
"hacker": "kracker96", }

def spr_credentiale(login, password):
 if login in credentiale and credentiale[login] == password:
     return True
 else:
     return False

login = input("Enter your login: ")
password = input("Enter your password: ")

if spr_credentiale(login, password):
    print("Login successful!")
else:
    print("Login failed. Invalid login or password.")
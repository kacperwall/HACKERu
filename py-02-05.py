adb = {
    "user": "password",
    "Admin": "Admin",
}

def Intro():
    intro = "Welcome to Messy CLI\n" \
            "Please Register OR Login\n" \
            "1.Login\n" \
            "2.Register\n" \
            "3.Quit\n"
    print(intro)
    return input("")

def Clear():
    i = 0
    while i < 30:
        print("\n")
        i = i + 1

def Auth(user, pswd):
    global adb
    for key in adb:
        if key == user and adb[key] == pswd:
            return True
    return False

def Reg():
    global adb
    user = input("Please Enter username\n==>")
    try:
        if Auth(user, adb[user]) == True:
            print("user is already exists")
    except:
        pswd = input("Please Enter The password\n==>")
        adb[user] = pswd
        print("Registered")

def Main():
    while True:
        wybor = Intro()
        if wybor == "1": # 3
            Clear()
            user = input("Please Enter Your Username\n==> ")
            pswd = input("Please Enter Your Password\n==> ")
            if Auth(user, pswd) == True:
                print("Welcome", user)
                break
            else:
                print("Wrong Login")Wawrzyniak
        elif wybor == "2": # znowu prosi o wybor 1
            Clear()
            Reg()
        elif wybor == "3":
            print("ByeBye")
            break
        else:
            print("Wrong Pick")


if __name__ == '__main__':
    Main()

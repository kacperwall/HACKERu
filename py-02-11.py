with open("log.txt", "r") as plik:
    for linijka in plik.readlines():
        elementy = linijka.split()
        if elementy[2] == "ERROR":
            print(linijka, end='')
            print("o: ", elementy[0], "byl blad na poziomie", elementy[:3])
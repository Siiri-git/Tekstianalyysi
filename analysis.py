# file = open("filename.txt", "r")
# lines = file.readlines()
txtFiles = {"artikkeli1.txt", "artikkeli1.txt", "artikkeli1.txt", "artikkeli1.txt"}

while True:
    usrFile = input("Tiedoston nimi (esim. nimi.tyyppi): ")
    if usrFile in txtFiles:
        with open(usrFile, 'r', encoding='utf-8') as file:
            content = file.read()
            wrds = content.split()
            count = len(wrds)
        # merkkien määrän tarkistus
        length = len(content)
        print(f"Tekstissä on {length} merkkejä\nTekstissä on {count} sanaa")

    else: # anna error viesti jos tiedostoa ei löydy 
          # ja pyydä yrittämään uuestaan
        print("! File not found.\nPlease try again.\n")
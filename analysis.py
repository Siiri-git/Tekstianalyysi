# file = open("filename.txt", "r")
# lines = file.readlines()
txtFiles = {"article1.txt", "article2.txt", "article3.txt", "article4.txt", "demofile.txt"}

while True:
    usrFile = input("File name: ")

    if usrFile in txtFiles:
        file = open(usrFile, "r")
        print(file.read())

    else: # anna error viesti jos tiedostoa ei löydy
        print("! File not found.\nPlease try again.\n")
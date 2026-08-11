# file = open("filename.txt", "r")
# lines = file.readlines()
txtFiles = {"article1.txt", "article2.txt", "article3.txt", "article4.txt"}
lines =words = chars = spaces = 0
while True:
    usrFile = input("File name: ")
    if usrFile in txtFiles:
        print("Yay")

    else: # anna error viesti jos tiedostoa ei löydy
        print("! File not found.\nPlease try again.\n")
# file = open("filename.txt", "r")
# lines = file.readlines()
txtFiles = {"article1", "article2", "article3", "article4", "demofile"}

while True:
    print("Functions:\n1. Find a file\n2. Exit")
    usrFunc = input("Choose a function: ")

    if usrFunc == "1":
        usrFile = input("File name: ")
        if usrFile in txtFiles:
            print("yay")
            file = open(usrFile, "r")

        else:
            print("try again")

    elif usrFunc == "2":
        break

    else:
        print("Try again!")
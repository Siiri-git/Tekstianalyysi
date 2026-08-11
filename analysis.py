# file = open("filename.txt", "r")
# lines = file.readlines()
txtFiles = {"article1", "article2", "article3", "article4"}

while True:
    print("Functions:\n1. Find a file\n2. Exit")
    usrFunc = input("Choose a function: ")

    if usrFunc == "1":
        usrFile = input("File name: ")


    elif usrFunc == "2":
        break
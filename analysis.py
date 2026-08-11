import heapq
from collections import Counter
txtFiles = {"artikkeli1.txt", "artikkeli2.txt", "artikkeli3.txt", "artikkeli4.txt"}

while True:
    usrFile = input("Tiedoston nimi (esim. nimi.tyyppi): ")
    if usrFile in txtFiles:
        with open(usrFile, 'r', encoding='utf-8') as file:
            content = file.read()
            wrds = content.split()
            wrdCount = len(wrds)
        # merkkien määrän tarkistus
        chars = len(content)
        # yleisimmät sanat
        cnt = Counter(wrds)
        k = 5
        top_k = heapq.nlargest(k, cnt.items(), key=lambda x: x[1])
        topWrds = []
        for item in top_k:
            topWrds.append(item[0])
        # yleisimmät kirjiamet
        charFreq = {}
        for char in content.replace(" ","").lower():
            if char in charFreq:
                charFreq[char] += 1
            else:
                charFreq[char] = 1
        sortedCharFreq = dict(sorted(charFreq.items(), key=lambda item: item[1], reverse=True))
        listSoCaFr = []
        for char in sortedCharFreq:
            listSoCaFr.append(char)

        print(f"> Tekstissä on {chars} merkkiä\n> Tekstissä on {wrdCount} sanaa\n> Yleisimmät sanat ovat {', '.join(topWrds)}")
        print(f"> Yleisimmät merkit ovat {listSoCaFr[0]}, {listSoCaFr[1]}, {listSoCaFr[2]}, {listSoCaFr[3]}, {listSoCaFr[4]}")

    else: # anna error viesti jos tiedostoa ei löydy
          # ja pyydä yrittämään uuestaan
        print("! File not found.\nPlease try again.\n")
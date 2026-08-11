# oettaan python kirjastosta eri toiminto juttuja käyttöön
import heapq
from collections import Counter
# lista jossa on käytettävän tiedosto nimer
txtFiles = {"artikkeli1.txt", "artikkeli2.txt", "artikkeli3.txt", "artikkeli4.txt"}

while True:
    # pyydetään käyttäjän tiedoston nimi
    usrFile = input("Tiedoston nimi (esim. nimi.tyyppi): ")
    if usrFile in txtFiles: # jos käyttäjän tiedosto löytyy tiedosto listasta
        with open(usrFile, 'r', encoding='utf-8') as file:
            content = file.read() # luetaan sisältö ja laitetaan se "content" muuttujaan
            wrds = content.split() # splitataan "content" eli erotellaan sanat muuttujaan "wrds"
            wrdCount = len(wrds) # asetetaan sanojen määrä "wrdCount" muuttujaan
        # merkkien määrän tarkistus
        chars = len(content) # sisällön määrä ("content") pituus asetetaan merkkeihin
        # eli lasketaan merkkien määrä
        # yleisimmät sanat
        cnt = Counter(wrds) # lasketaan jokaisen sanan määrä ja asetetaan ne "cnt" muuttujaan
        amount = 5 # "amount" arvo on 5
        # heapq.nlargest palauttaa 5 ("amount") suurinta arvoa (katsoo cnt.items)
        # ja ne laitetaan "topAmount" muuttujaan (lista)
        topAmount = heapq.nlargest(amount, cnt.items(), key=lambda x: x[1])
        topWrds = [] # luodaan tyhjä lista
        for item in topAmount: # käydään läpi "topAmount" listan tuotteet
            topWrds.append(item[0]) # lisätään niiden ensimmäinen item "topWrds" listaan
        # yleisimmät kirjiamet
        charFreq = {} # tyhjä dictionary "charFreq"
        for char in content.replace(" ","").lower(): # käydään "content" läpi ja korvataan välit pois ja kirjaimet pieniksi
            # katsotaan kirjaimet läpi ja lisätään niiden määrä aina jos se toistuu
            if char in charFreq:
                charFreq[char] += 1
            else:
                charFreq[char] = 1
        sortedCharFreq = dict(sorted(charFreq.items(), key=lambda item: item[1], reverse=True))
        listSoCaFr = [] # tyhjä "soterCharFreq" lista
        for char in sortedCharFreq: # käydään "sortedCharFreq" läpi
            listSoCaFr.append(char) # lisätään kirjaimet "listSoCaFr" listaan top5 kirjaimet

        # tulostetaan kaikkii tiedot
        print(f"> Tekstissä on {chars} merkkiä\n> Tekstissä on {wrdCount} sanaa\n> Yleisimmät sanat ovat {', '.join(topWrds)}")
        print(f"> Yleisimmät merkit ovat {listSoCaFr[0]}, {listSoCaFr[1]}, {listSoCaFr[2]}, {listSoCaFr[3]}, {listSoCaFr[4]}")

    else: # anna error viesti jos tiedostoa ei löydy
          # ja pyydä yrittämään uuestaan
        print("! File not found.\nPlease try again.\n")
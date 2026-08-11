import collections

while True:
    nimi = input("Anna tekstitiedoston nimi: ")

    try:
        with open(nimi, "r", encoding="utf-8") as f:
            teksti = f.read()
        break
    except FileNotFoundError:
        print("Tiedostoa ei löydy.")

# Merkkien määrä
merkit = len(teksti)
print(f"Tekstissä on {merkit} merkkiä.")

# Sanat
sanat = teksti.split()
sanamaara = len(sanat)
print(f"Tekstissä on {sanamaara} sanaa.")

# Yleisimmät sanat
sanat_pienilla = [s.lower() for s in sanat]
yleisimmat_sanat = collections.Counter(sanat_pienilla).most_common(5)
yleisimmat_sanat_lista = [sana for sana, maara in yleisimmat_sanat]
print("Yleisimmät sanat ovat " + ", ".join(yleisimmat_sanat_lista[:-1]) +
      " ja " + yleisimmat_sanat_lista[-1] + ".")

# Yleisimmät merkit (poislukien välilyönnit)
merkit_ilman_valilyonteja = [m for m in teksti.lower() if m != " "]
yleisimmat_merkit = collections.Counter(merkit_ilman_valilyonteja).most_common(5)
yleisimmat_merkit_lista = [m for m, maara in yleisimmat_merkit]
print("Yleisimmät merkit ovat " + ", ".join(yleisimmat_merkit_lista[:-1]) +
      " ja " + yleisimmat_merkit_lista[-1] + ".")

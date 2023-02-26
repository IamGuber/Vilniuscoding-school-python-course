# Susikurkite sąrašą failų pavadinimams saugoti, užpildykite jį duomenimis. 
# Įsivaizduokite kad jums reikės nuskaityti šiuos failus, todėl pirma norėsite patikrinti su kuriais galite dirbti. 
# Atrinkite į atskirą sąrašą tik tuos failus, kurių galūnė yra .txt arba .json tipo. Išveskite atrinktus duomenis.

sarasas = [".pdf", ".py", ".doc", ".txt", ".json"]
tuscias = []

klausymas = input("Norite pamatyti visa failu sarasa? Y/N: ")
if klausymas == "Y":
    print(sarasas)
else:
    print()

for failas in sarasas:
    klausymas2 = input("Kokio failo ieskote?: ")
    if klausymas2 in sarasas:
        print("Jeigu norite baigti paieska, iveskite '0'.")
        tuscias.append(klausymas2)
    if klausymas2 == "0":
        break

print("Suradote ir pridejote situos failus:", tuscias)
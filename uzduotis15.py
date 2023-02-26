# Susikurkite sąrašą, kuriame būtų saugoma keleto įmonių duomenys (kaip dictionary elementai) 
# ir jį užpildykite duomenimis. Išveskite kiekvienos įmonės informaciją atskirose eilutėse, gražiai suformatuotai 
# (sakinio pavidalu ar pan.). Taip pat, ką nors paskaičiuokite iš turimų skaitinių duomenų 
# (pvz.: vidutinis įmonės amžius, darbuotojų kiekis per visas įmones, bendras pelnas, ar pan.).

sarasas = [
    {
        "imone" : "Transporteris",
        "pelnas" : 344890,
        "darbuotoju kiekis" : 128,
        "imones automobiliu" : 90,
        "imones priekabu" : 20,
        "veikla nuo" : 2010
    },
    {
        "imone" : "BestWay",
        "pelnas" : 431765,
        "darbuotoju kiekis" : 70,
        "imones automobiliu" : 66,
        "imones priekabu" : 78,
        "veikla nuo" : 2017
    },
    {
        "imone" : "JuodasKelias",
        "pelnas" : 155990,
        "darbuotoju kiekis" : 166,
        "imones automobiliu" : 56,
        "imones priekabu" : 7,
        "veikla nuo" : 2008
    },
    {
        "imone" : "MaxOnIT",
        "pelnas" : 244672,
        "darbuotoju kiekis" : 15,
        "imones automobiliu" : 5,
        "imones priekabu" : 88,
        "veikla nuo" : 2012
    }
]

print("Pirma imone sarase yra", sarasas[0]["imone"], "." "\n" "Imone ikurta", sarasas[0]["veikla nuo"], "metais. Darbuotoju skaicius siuo metu yra", 
sarasas[0]["darbuotoju kiekis"], "zmones.", sarasas[0]["imone"], "turi nuosava automobilio parka.", sarasas[0]["imones automobiliu"], "automobiliai o taip ir",
sarasas[0]["imones priekabu"], "priekabu." "\n" "Imones pelnas yra", sarasas[0]["pelnas"], "eur.")
print()
print("Antra imone sarase yra", sarasas[1]["imone"], "." "\n" "Imone ikurta", sarasas[1]["veikla nuo"], "metais. Darbuotoju skaicius siuo metu yra", 
sarasas[1]["darbuotoju kiekis"], "zmones.", sarasas[1]["imone"], "turi nuosava automobilio parka.", sarasas[1]["imones automobiliu"], "automobiliai o taip ir",
sarasas[1]["imones priekabu"], "priekabu." "\n" "Imones pelnas yra", sarasas[1]["pelnas"], "eur.")
print()
print("Trecia imone sarase yra", sarasas[2]["imone"], "." "\n" "Imone ikurta", sarasas[2]["veikla nuo"], "metais. Darbuotoju skaicius siuo metu yra", 
sarasas[2]["darbuotoju kiekis"], "zmones.", sarasas[2]["imone"], "turi nuosava automobilio parka.", sarasas[2]["imones automobiliu"], "automobiliai o taip ir",
sarasas[2]["imones priekabu"], "priekabu." "\n" "Imones pelnas yra", sarasas[2]["pelnas"], "eur.")
print()
print("Ketvirta imone sarase yra", sarasas[2]["imone"], "." "\n" "Imone ikurta", sarasas[2]["veikla nuo"], "metais. Darbuotoju skaicius siuo metu yra", 
sarasas[2]["darbuotoju kiekis"], "zmones.", sarasas[2]["imone"], "turi nuosava automobilio parka.", sarasas[2]["imones automobiliu"], "automobiliai o taip ir",
sarasas[2]["imones priekabu"], "priekabu." "\n" "Imones pelnas yra", sarasas[2]["pelnas"], "eur.")

print()

bendras_pelnas = 0
for i in sarasas:
    bendras_pelnas += i["pelnas"]
print("Bendras imoniu pelnas yra:", bendras_pelnas, "eur.")

print()

darb_sum = 0
for i in sarasas:
    darb_sum += i["darbuotoju kiekis"]
vid_darb_skc = round(darb_sum / len(sarasas), 0)
print("Vidutinis imoniu darbuotoju skaicius:", vid_darb_skc, "zmoniu.")

print()

bendras_amzius = 0
for i in sarasas:
    bendras_amzius += 2022 - i["veikla nuo"]
vid_amzius = round(bendras_amzius / len(sarasas), 1)
print("Vidutinis imoniu amzius yra", vid_amzius, "metu.")
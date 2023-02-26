# Susikurkite dictionary, kuriame būtų nurodytos prekės ir turimi kiekiai, t.y. 
# raktas yra prekės pavadinimas ir reikšmė yra turimas prekės kiekis, o visa tai saugoma viename dictionary 
# (panašu į 29 pavyzdį). Išveskite visą turimą dictionary informaciją gražiai suformatuotai, 
# pvz: '- Prekės "Pieštukas" liko 132 vnt.' ir tai padaryti atskirose eilutėse. 
# Taip pat, raskite ir išveskite visų prekių bendrą turimą kiekį (sudėti visus turimus kiekius), 
# kiekių vidurkį (kiek vidutiniškai turima prekių). O tos prekės kurios likę mažiausiai vienetų išvesti pavadinimą ir kiekį.

info = {
    "duona" : 14,
    "pienas" : 6,
    "bananai" : 2,
    "mineralinis vanduo" : 22,
    "kava" : 11
}

for i in info:
    print("preke:", i, "liko", info[i], "vnt.")

print("Is viso prekiu likutis:", sum(info.values()))
print("Prekiu kiekio vidurkis:", sum(info.values()) / len(info.values()))

print("Prekes kuriu liko maziau nei 10:")
for i, y in info.items():
    if y < 10:
        print(i, y)
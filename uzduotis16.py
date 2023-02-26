# Susikurkite sąrašą, kuriame būtų saugoma informacija apie skirtingas ligonines (kaip dictionary elementai) 
# ir užpildykite jį pasirinktais duomenimis. Išveskite ligoninių pavadinimus su adresais skirtingose eilutėse. 
# Suskaičiuokite ką nors iš skaitinių jų duomenų, pvz.: bendrą lankytojų kiekį, bendrą ar vidutinį darbuotojų kiekį, ar pan.

ligonines = [
    {
        "pavadinimas" : "Pirmoji centrine ligonine",
        "adresas" : "klaipedos g. 41",
        "gydytoju kiekis" : 98,
        "ligoniu kiekis" : 789
    },
    {
        "pavadinimas" : "Rajonine ligonine",
        "adresas" : "jokubo g. 3",
        "gydytoju kiekis" : 51,
        "ligoniu kiekis" : 414
    },
    {
        "pavadinimas" : "Pagrindine ligonine",
        "adresas" : "menuolio g. 112",
        "gydytoju kiekis" : 64,
        "ligoniu kiekis" : 564
    }
]

for i in ligonines:
    print("Ligonine", i["pavadinimas"], "randasi pagal adresa", i["adresas"])

bendr_gydyt = 0
for i in ligonines:
    bendr_gydyt += i["gydytoju kiekis"]
print("Bendras ligoniniu gydytoju kiekis:", bendr_gydyt)

vid_ligon = 0
for i in ligonines:
    vid_ligon += i["ligoniu kiekis"]
bendras_ligon = vid_ligon / len(ligonines)
print("Vidutinis ligoniu skaicius visu ligoniniu yra:", bendras_ligon)
# Susikurkite pasirinktą csv failą ir užpildykite jį duomenimis. Pamėginkite jį nuskaityti su reader ir su DictReader. 
# Iš šio failo duomenų išsiskaičiuokite bent 2 pasirinktus dalykus (pvz studentų vidurkių vidurkį, rasti žemiausią studentą, ar pan.). 
# Nuskaitytus duomenis ir gautus rezultatus išveskite ekrane.

from csv import reader

with open("/Users/guber/Desktop/python mokymai/19-darbas-su-failais/Studentai.csv") as failas:
    studentai = reader(failas)
    studentai = reader(failas, delimiter=",")
    next(studentai)
    for i in studentai:
        print(i)

from csv import DictReader

sarasas = []
with open("/Users/guber/Desktop/python mokymai/19-darbas-su-failais/Studentai.csv") as failas:
    studentai = DictReader(failas)
    studentai = DictReader(failas, delimiter=";")
    suma = 0
    kiekis = 0
    for i in studentai:
        print(i)
        suma += int(i["Kursas"])
        kiekis += 1
        sarasas.append(i)
    vidurkis = suma / kiekis
    print("Kursu vidurkis:", vidurkis)
if sarasas[0]["Kursas"] > sarasas[1]["Kursas"] and sarasas[0]["Kursas"] > sarasas[2]["Kursas"]:
    print(sarasas[0]["Vardas"], sarasas[0]["Pavarde"], "mokosi ilgiausiai.")
elif sarasas[0]["Kursas"] < sarasas[1]["Kursas"] and sarasas[1]["Kursas"] > sarasas[2]["Kursas"]:
    print(sarasas[1]["Vardas"], sarasas[1]["Pavarde"], "mokosi ilgiausiai.")
elif sarasas[2]["Kursas"] > sarasas[1]["Kursas"] and sarasas[0]["Kursas"] < sarasas[2]["Kursas"]:
    print(sarasas[2]["Vardas"], sarasas[2]["Pavarde"], "mokosi ilgiausiai.")

if sarasas[0]["Kursas"] < sarasas[1]["Kursas"] and sarasas[0]["Kursas"] < sarasas[2]["Kursas"]:
    print(sarasas[0]["Vardas"], sarasas[0]["Pavarde"], "mokosi trumpiausiai.")
elif sarasas[0]["Kursas"] > sarasas[1]["Kursas"] and sarasas[1]["Kursas"] < sarasas[2]["Kursas"]:
    print(sarasas[1]["Vardas"], sarasas[1]["Pavarde"], "mokosi trumpiausiai.")
elif sarasas[2]["Kursas"] < sarasas[1]["Kursas"] and sarasas[0]["Kursas"] > sarasas[2]["Kursas"]:
    print(sarasas[2]["Vardas"], sarasas[2]["Pavarde"], "mokosi trumpiausiai.")
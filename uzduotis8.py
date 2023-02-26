# Susikurkite du dictionary, dviejų studentų informacijai saugoti. 
# Abiejuose dictionary sudėkite šias savybes su reikšmėmis: vardas ir pavardė, studijų programos pavadinimas, pažymiai. 
# Raskite abiejų studentų pažymių vidurkius. Išveskite abiejų studentų informaciją, bei pažymių vidurkius. 
# Raskite ir išveskite, kurio studento pažymių vidurkis yra didesnis ir išveskite jo vardą su pavarde.

student1 = {
    "vardas" : "Jonas",
    "pavarde" : "Jonauskas",
    "studiju programos pavadinimas" : "Matematika",
    "pazymiai" : [10, 7, 8, 5, 4]
}

student2 = {
    "vardas" : "Petras",
    "pavarde" : "Petrauskas",
    "studiju programos pavadinimas" : "Fizika",
    "pazymiai" : [9, 10, 10, 5, 6]
}

vidurkis1 = sum(student1["pazymiai"]) / len(student1["pazymiai"])
vidurkis2 = sum(student2["pazymiai"]) / len(student2["pazymiai"])

print(student1)
print()
print("Pirmo studento pazymiu vidurkis:", vidurkis1)
print()
print(student2)
print()
print("Antro studento pazymiu vidurkis:", vidurkis2)
print()

if vidurkis1 > vidurkis2:
    print("Studento", student1["vardas"], student1["pavarde"], "vidurkis yra didesnis.")
elif vidurkis1 < vidurkis2:
    print("Studento", student2["vardas"], student2["pavarde"], "vidurkis yra didesnis.")
else:
    print("Abieju studentu vidurkiai vienodi.")
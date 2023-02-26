# Susikurkite sąrašą, kuriame būtų saugoma informacija apie keletą studentų 
# (kaip dictionary elementai), kur apie kiekvieną studentą būtų žinoma ši 
# informacija: vardas ir pavardė, amžius, pažymiai, studijų programa, kursas. 
# Kiekvieną studentą išveskite taip: pirmoje eilutėje visi studento duomenys išskyrus jo pažymius, 
# antroje eilutėje jo pažymiai, trečioje jo pažymių vidurkis su prierašu 'pažymių vidurkis'. 
# Išvedus visus studentus dėkite brūkšnį (pvz.: -----) ir išveskite bendrą visų studentų pažymių vidurkį.

studentai = [
    {
        "vardas" : "Julius",
        "pavarde" : "Juliauskas",
        "amzius" : 18,
        "pazymiai" : [10, 9, 8, 7, 6],
        "studiju programa" : "Matematika",
        "kursas" : 1
    },
    {
        "vardas" : "Ramune",
        "pavarde" : "Ramunskaite",
        "amzius" : 19,
        "pazymiai" : [10, 10, 7, 9, 8, 10],
        "studiju programa" : "Fizika",
        "kursas" : 3
    },
    {
        "vardas" : "Petras",
        "pavarde" : "Petrauskas",
        "amzius" : 21,
        "pazymiai" : [4, 5, 8, 9, 10, 10],
        "studiju programa" : "Chemija",
        "kursas" : 4 
    }
]

bendras_vidurkis = 0

for i in studentai:
    suma = sum(i["pazymiai"])
    vidurkis = round(suma / len(i["pazymiai"]), 1)
    bendras_vidurkis += vidurkis
    print("Studento vardas", i["vardas"], "pavarde" ,i["pavarde"], i["amzius"], "metu.", "Studiju programa:", 
    i["studiju programa"], "mokosi", i["kursas"], "-ame kurse." "\n" "Pazymiai:", i["pazymiai"], "\n" "Vidurkis:", vidurkis)

print("--------------------------------")
print("Bendras visus studentu vidurkis:", bendras_vidurkis)
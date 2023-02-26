# Susikurkite sąrašą, kuriame būtų saugoma informacija apie keletą automobilių (kaip dictionary elementai) 
# ir užpildykite jį pasirinktais duomenimis. Išveskite kiekvieno automobilio pavadinimą, metus ir paskaičiuotą 
# jo amžių (dabartiniai metai - gamybos metai).

import datetime

auto = [
    {
        "marke" : "Mercedes-Benz",
        "modelis" : "SL",
        "pagaminimo metai" : 2015,
        "darbinis turis" : 4.0,
        "spalva" : "juoda" 
    },
    {
        "marke" : "BMW",
        "modelis" : "3",
        "pagaminimo metai" : 2012,
        "darbinis turis" : 3.0,
        "spalva" : "sidabrine"
    },
    {
        "marke" : "Audi",
        "modelis" : "A6",
        "pagaminimo metai" : 2010,
        "darbinis turis" : 2.8,
        "spalva" : "balta" 
    }
]

metai1 = datetime.date.today().year - auto[0]["pagaminimo metai"]
metai2 = datetime.date.today().year - auto[1]["pagaminimo metai"]
metai3 = datetime.date.today().year - auto[2]["pagaminimo metai"]

print("Pirmas automobilis:", auto[0], "sitam automobiliui", metai1, "metu.\n")
print("Antras automobilis:", auto[1], "sitam automobiliui", metai2, "metu.")
print()
print("Trecias automobilis:", auto[2], "sitam automobiliui", metai3, "metu.")
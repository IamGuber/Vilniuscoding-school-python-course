# Susikurkite parduotuvės dictionary, kuriame būtų ši informacija: pavadinimas, adresas, darbuotojų kiekis, 
# prekių sąrašas (kiekviena kaip dictionary elementas). Apie kiekvieną prekę parduotuvėje 
# žinoma ši informacija: pavadinimas; kodas; kaina; savikaina; turimas kiekis. Išveskite parduotuvės bendrą informaciją, 
# tuomet užrašą "prekės" ir atskirose eilutėse turimas prekes su kuria nors jų informacija (pvz.: pavadinimai,
# kainos ir turimi kiekiai). Galiausiai paskaičiuokite kiek iš viso parduotuvė turi visų prekių (sudėkite jų kiekius). 
# Raskite ir išveskite kurios prekės turima daugiausiai, o kurios mažiausiai.

info = {
    "pavadinimas" : "Viskas vietoje",
    "adresas" : "linkmenu g. 3B", 
    "darbuotoju kiekis" : 12,
    "prekiu sarasas" : {
        "preke1" : {
            "pavadinimas" : "Monitorius",
            "kodas" : "m023",
            "kaina" : 240,
            "savikaina" : 160,
            "turimas kiekis" : 5
        },
        "preke2" : {
            "pavadinimas" : "Klaviatura",
            "kodas" : "k156",
            "kaina" : 100,
            "savikaina" : 60,
            "turimas kiekis" : 12
        },
        "preke3" : {
            "pavadinimas" : "Pele",
            "kodas" : "p390",
            "kaina" : 70,
            "savikaina" : 50,
            "turimas kiekis" : 30
        }
    }
}

print("Parduotuve:", info["pavadinimas"], "\n" "adresas:", info["adresas"], "\n" "darbuotoju:", 
info["darbuotoju kiekis"], "zmoniu.")

print("Prekes:")
print(info["prekiu sarasas"]["preke1"]["pavadinimas"])
print(info["prekiu sarasas"]["preke1"]["kaina"], "eur.")
print(info["prekiu sarasas"]["preke1"]["turimas kiekis"], "vnt.")
print()
print(info["prekiu sarasas"]["preke2"]["pavadinimas"])
print(info["prekiu sarasas"]["preke2"]["kaina"], "eur.")
print(info["prekiu sarasas"]["preke2"]["turimas kiekis"], "vnt.")
print()
print(info["prekiu sarasas"]["preke3"]["pavadinimas"])
print(info["prekiu sarasas"]["preke3"]["kaina"], "eur.")
print(info["prekiu sarasas"]["preke3"]["turimas kiekis"], "vnt.")

bendras_kiekis = 0
for i in info["prekiu sarasas"].values():
    bendras_kiekis += i["turimas kiekis"]
print("Bendras prekiu skaicius:", bendras_kiekis)

if info["prekiu sarasas"]["preke1"]["turimas kiekis"] > info["prekiu sarasas"]["preke2"]["turimas kiekis"] and info["prekiu sarasas"]["preke1"]["turimas kiekis"] > info["prekiu sarasas"]["preke3"]["turimas kiekis"]:
    print("Monitoriaus sandelyje daugiausia.")
elif info["prekiu sarasas"]["preke1"]["turimas kiekis"] < info["prekiu sarasas"]["preke2"]["turimas kiekis"] and info["prekiu sarasas"]["preke2"]["turimas kiekis"] > info["prekiu sarasas"]["preke3"]["turimas kiekis"]:
    print("Klaviaturu sandelyje daugiausia.")
elif info["prekiu sarasas"]["preke1"]["turimas kiekis"] < info["prekiu sarasas"]["preke3"]["turimas kiekis"] and info["prekiu sarasas"]["preke2"]["turimas kiekis"] < info["prekiu sarasas"]["preke3"]["turimas kiekis"]:
    print("Peliu sandelyje daugiausia.")

if info["prekiu sarasas"]["preke1"]["turimas kiekis"] < info["prekiu sarasas"]["preke2"]["turimas kiekis"] and info["prekiu sarasas"]["preke1"]["turimas kiekis"] < info["prekiu sarasas"]["preke3"]["turimas kiekis"]:
    print("Monitoriaus sandelyje maziausiai.")
elif info["prekiu sarasas"]["preke1"]["turimas kiekis"] > info["prekiu sarasas"]["preke2"]["turimas kiekis"] and info["prekiu sarasas"]["preke2"]["turimas kiekis"] < info["prekiu sarasas"]["preke3"]["turimas kiekis"]:
    print("Klaviaturu sandelyje maziausiai.")
elif info["prekiu sarasas"]["preke1"]["turimas kiekis"] > info["prekiu sarasas"]["preke3"]["turimas kiekis"] and info["prekiu sarasas"]["preke2"]["turimas kiekis"] > info["prekiu sarasas"]["preke3"]["turimas kiekis"]:
    print("Peliu sandelyje maziausiai.")
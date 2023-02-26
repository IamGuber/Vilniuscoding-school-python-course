# Sukurkite dictionary informacijai apie filmą saugoti. 
# Į šį dictionary sudėkite tokias savybes su reikšmėmis: pavadinimas, režisierius, biudžetas, 
# kiek uždirbo pinigų po išleidimo, žanras, trukmė, išleidimo metai, aktorių sąrašas (masyvas su jų vardais ir pavardėmis). 
# Išveskite šio dictionary informaciją. Paskaičiuokite ir išveskite šio filmo pelną (uždarbis - biudžetas). 
# Išveskite kiek filme dalyvavo aktorių (jų kiekis). 
# Paskaičiuokite kiek filmui yra metų 
# (dabartinius metus tiesiog galite įrašyti rankomis arba panaudoti datetime.date.today().year funkciją, 
# pačiame failo viršuje reikės nurodyti import datetime).

info = {
    "pavadinimas" : "Trileris",
    "rezisierius" : "Jonas",
    "biudzetas" : 1000000,
    "uzdirbti pinigai" : 3000000,
    "zanras" : "istorinis",
    "trukme" : 120,
    "isledimo metai" : 2020,
    "aktoriu sarasas" : ["Petras", "Paulius", "Viktorija", "Julija"],
}

uzdarbis = info["uzdirbti pinigai"] - info["biudzetas"]
metai = 2022 - info["isledimo metai"]
print("Filmo uzdarbis:", uzdarbis)
print("FIlme dalyvavo", len(info["aktoriu sarasas"]), "aktoriai.")
print("Filmui yra", metai, "metai.")
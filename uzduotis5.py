# Sukurkite dictionary automobilio duomenims saugoti. Į šį dictionary savybes su reikšmėmis sukelkite, 
# po to kai sukursite tuščią dictionary (14-as pavyzdys). Sudėkite šias savybes su reikšmėmis: markė, modelis, 
# rida, gamybos metai, spalva, darbinis tūris, ar daužta, ar parduodama. Išveskite visą automobilio informaciją. 
# Paskaičiuokite ir išveskite kiek automobiliui yra metų 
# (rankomis įrašykite dabartinius metus arba panaudokite datetime.date.today().year funkciją, pačiame failo viršuje 
# reikės nurodyti import datetime). Paskaičiuokite ir išveskite kiek vidutiniškai per metus yra nuvažiavęs automobilis 
# (jeigu viso nuvažiavo 300 kilometrų, o automobiliui yra 2 metai, tai per metus vidutiniškai gaunasi 150 km.).

import datetime

info = {}

info["marke"] = "BMW"
info["modelis"] = "7"
info["rida"] = 145000
info["gamybos metai"] = 2016
info["spalva"] = "juoda"
info["darbinis turis"] = 3.0
info["ar dauzta"] = False
info["ar parduodama"] = True

print(info)

metai = datetime.date.today().year - info["gamybos metai"]
km_per_metus = round(info["rida"] / metai, 1)

print("Automobiliui yra", metai, " metai. Vidutiniskai per metus pravaziavo:", km_per_metus, "km.")
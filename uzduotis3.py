# Sukurkite du dictionary dviejų knygų informacijai saugoti. 
# Kiekviename dictionary nurodykite tokias savybes su reikšmėmis: pavadinimas, autorius, žanras, kaina, puslapių kiekis, 
# skyrių sąrašas (masyvas su pavadinimais), išleidimo metai, ar knygą galima rasti knygynuose. Išveskite šių knygų informaciją. 
# Išveskite kuri knyga plonesnė (turi mažiau puslapių), bei kurioje knygoje yra daugiau skyrių. 
# Paskaičiuokite, jeigu pigesnės knygos kainą padvigintumėte, ar ji jau būtų brangesnė už kitą knygą?

info = {
    "knyga1" : {
        "pavadinimas" : "Jureivis",
        "aktorius" : "Jonas",
        "zanras" : "romanas",
        "kaina" : 20.19,
        "puslapiu kiekis" : 412,
        "skyriu sarasas" : ["pirmas", "antras", "trecias", "ketvirtas", "penktas"],
        "isledimo metai" : 2016,
        "ar galima rasti knygynuose" : True,
    },
    "knyga2" : {
        "pavadinimas" : "Kitama kraste",
        "aktorius" : "Petras",
        "zanras" : "detektyvas",
        "kaina" : 24.79,
        "puslapiu kiekis" : 389,
        "skyriu sarasas" : ["vienas", "du", "trys", "keturi", "penki", "sesi"],
        "isledimo metai" : 2020,
        "ar galima rasti knygynuose" : False,
    }
}

print("Info apie pirma knyga:", info["knyga1"])
print()
print("Info apie antra knyga:", info["knyga2"])

print()

if info["knyga1"]["puslapiu kiekis"] > info["knyga2"]["puslapiu kiekis"]:
    print("Pirma knyga yra storesne nei antra.")
elif info["knyga1"]["puslapiu kiekis"] < info["knyga2"]["puslapiu kiekis"]:
    print("Antra knyga yra storesne nei pirma.")
else:
    print("Abi knygos yra vienos pagal storuma.")

if len(info["knyga1"]["skyriu sarasas"]) > len(info["knyga2"]["skyriu sarasas"]):
    print("Pirma knyga turi daugiau skyriu.")
elif len(info["knyga1"]["skyriu sarasas"]) < len(info["knyga2"]["skyriu sarasas"]):
    print("Antra knyga turi daugiau skyriu.")
else:
    print("Abi knygos turi vienoda skyriu kieki.")

print()
print("Jeigu pirmos knygos kaina butu dvigubai didesne, ar jinai butu brangesne uz antra knyga?")

if info["knyga1"]["kaina"] * 2 > info["knyga2"]["kaina"]:
    print("Pirma knyga butu brangesne")


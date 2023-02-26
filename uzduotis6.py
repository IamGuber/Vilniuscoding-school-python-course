# Sukurkite ir iškvieskite funkciją, kurioje kintamuosiuose būtų saugoma informacija apie policininką 
# (vardas, pavardė, amžius, alga, etatas, specializacija). Išveskite šią informaciją suformatuotai 
# (pavyzdžiui įterpkite į sakinį, ar išveskite sąrašu ar pan.).

def info():
    vardas = "Jonas"
    pavarde = "Jonaitis"
    amzius = 30
    alga = 1500
    etatas = 0.75
    specializacija = "Kriminalistas"
    print(f"Policininkas {vardas} dirba policijoje. Jam yra {amzius}. Dirba {etatas} etato. Metine alga yra: {alga * 12} eur.\n")
    sarasas = [vardas, pavarde, amzius, alga, etatas, specializacija]
    print("Visa informacija apie darbuotoja:\n", sarasas)

info()
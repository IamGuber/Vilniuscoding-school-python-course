# Susikurkite dictionary informacijai apie knygyną saugoti. 
# Į šį dictionary sudėkite tokias savybes su reikšmėmis: pavadinimas, adresas, plotas (kv. m.), 
# kiek turi knygų, darbo valandos, ar atidarytas. Išveskite šio knygyno dictionary raktus su reikšmėmis.

info = {
    "pavadinimas" : "Poseidonas",
    "adresas" : "Upes g. 14",
    "plotas (kv. m.)" : 80,
    "kiek knygu" : 145,
    "darbo valandos" : "10val. - 22val.",
    "ar atidarytas" : True
}

for i in info.items():
    print(i)
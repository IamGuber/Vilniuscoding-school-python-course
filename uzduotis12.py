# Susikurkite sąrašą, kuriame būtų saugomos skirtingos knygos (kaip dictionary elementai). 
# Apie kiekvieną knygą į atskirus knygų dictionary sudėkite norimą informaciją (bent 3 savybes). 
# Į list įdėkite bent 3 knygas. Visas šias knygas išsiveskite. Tuomet parodykite pirmą knygą. Antros knygos kažkurią savybę.

knygos = [
    {
        "pavadinimas" : "Viskas apie katinus",
        "aktorius" : "Ramune Ramunaite",
        "kaina" : 15.99,
    },
    {
        "pavadinimas" : "Nebent karta gyvenime",
        "aktorius" : "Jonas Jonauskas",
        "kaina" : 22,
    },
    {
        "pavadinimas" : "Tamsus kelias",
        "aktorius" : "Jonas Jinkauskas",
        "kaina" : 25.99,
    }
]

print(knygos)
print("Pirma knyga sarase:", knygos[0])
print("Antros knygos kaina:", knygos[1]["kaina"], "eur.")
# Susikurkite sąrašą, kuriame būtų keletas prekių (kaip dictionary elementai) ir jį užpildykite pasirinktais duomenimis. 
# Išveskite visų prekių pavadinimus su kainomis ir dar kokiais nors atributais atskirose eilutėse.

sarasas = [
    {
        "preke" : "Monitorius",
        "kaina" : 220,
        "ar yra sandelyje" : False,
        "pagaminimo metai" : 2020
    },
    {
        "preke" : "Kompiuteris",
        "kaina" : 2100,
        "ar yra sandelyje" : True,
        "pagaminimo metai" : 2021
    },
    {
        "preke" : "Telefonas",
        "kaina" : 999,
        "ar yra sandelyje" : True,
        "pagaminimo metai" : 2022
    },
    {
        "preke" : "Plansetas",
        "kaina" : 150,
        "ar yra sandelyje" : False,
        "pagaminimo metai" : 2019
    }
]

for i in sarasas:
    print(i)
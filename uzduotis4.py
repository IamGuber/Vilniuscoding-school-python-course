# Sukurkite tris dictionary prekių duomenims saugoti. Kiekviename dictionary sudėkite šias savybes su reikšmėmis: 
# pavadinimas, kaina, savikaina, kodas, turimas kiekis sandėlyje, siuntimui dėžės matmenys (x, y, z ašys). 
# Išveskite visų trijų prekių informaciją. Išveskite visų prekių kainas vienoje eilutėje (pirma prekė kainuoja - …, 
# antra prekė kainuoja - …, ir t.t.). Raskite ir išveskite kuri prekė yra brangiausia 
# (jos pavadinimą ir kainą arba visą rastos prekės informaciją). 
# Raskite ir išveskite atskirose eilutėse kiekvienos prekės dėžės tūrį. 
# Raskite ir išveskite atskirose eilutėse kiekvienos prekės pelningumą ((kaina - savikaina) * kiekis sandėlyje).

info1 = {
    "pavadinimas" : "Flesiukas",
    "kaina" : 12,
    "savikaina" : 8,
    "kodas" : "f02",
    "turimas kiekis sandelyje" : 21,
    "deze siuntimui" : {
        "x-asys" : 5,
        "y-asys" : 2,
        "z-asys" : 1.5,
    }
}

info2 = {
    "pavadinimas" : "Klaviatura",
    "kaina" : 119,
    "savikaina" : 69,
    "kodas" : "kv34",
    "turimas kiekis sandelyje" : 8,
    "deze siuntimui" : {
        "x-asys" : 150,
        "y-asys" : 20,
        "z-asys" : 45,
    }
}

info3 = {
    "pavadinimas" : "Pele",
    "kaina" : 79,
    "savikaina" : 59,
    "kodas" : "p55",
    "turimas kiekis sandelyje" : 15,
    "deze siuntimui" : {
        "x-asys" : 25,
        "y-asys" : 20,
        "z-asys" : 15,
    }
}

print(info1, "\n")
print(info2, "\n")
print(info3, "\n")

print("Pirma preke kainuoja:", info1["kaina"], "eur.")
print("Antra preke kainuoja:", info2["kaina"], "eur.")
print("Trecia preke kainuoja:", info3["kaina"], "eur.")
print()

if info1["kaina"] > info2["kaina"] and info1["kaina"] > info3["kaina"]:
    print("Pirmos prekes kaina didziausia.", info1["pavadinimas"], info1["kaina"], "eur.")
elif info1["kaina"] < info2["kaina"] and info2["kaina"] > info3["kaina"]:
    print("Antros prekes kaina didziausia.", info2["pavadinimas"], info2["kaina"], "eur.")
elif info3["kaina"] > info2["kaina"] and info2["kaina"] < info3["kaina"]:
    print("Trecios prekes kaina didziausia.", info3["pavadinimas"], info3["kaina"], "eur.")
else:
    print("Prekiu kainos vienodos.")

print()

deze1 = info1["deze siuntimui"]["x-asys"] * info1["deze siuntimui"]["y-asys"] * info1["deze siuntimui"]["z-asys"]
deze2 = info2["deze siuntimui"]["x-asys"] * info2["deze siuntimui"]["y-asys"] * info2["deze siuntimui"]["z-asys"]
deze3 = info3["deze siuntimui"]["x-asys"] * info3["deze siuntimui"]["y-asys"] * info3["deze siuntimui"]["z-asys"]

print("Pirmos prekes dezes siuntimui turis:", deze1,)
print("Antros prekes dezes siuntimui turis:", deze2,)
print("Trecios prekes dezes siuntimui turis:", deze3, "\n")

pelnas1 = (info1["kaina"] - info1["savikaina"]) * info1["turimas kiekis sandelyje"]
pelnas2 = (info2["kaina"] - info2["savikaina"]) * info2["turimas kiekis sandelyje"]
pelnas3 = (info3["kaina"] - info3["savikaina"]) * info3["turimas kiekis sandelyje"]

print("Pirmos prekes pelningumas:", pelnas1, "eur.")
print("Pirmos prekes pelningumas:", pelnas2, "eur.")
print("Pirmos prekes pelningumas:", pelnas3, "eur.")
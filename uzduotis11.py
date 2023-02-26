# Kaimynystėje yra trys kepyklos, apie kiekvieną yra žinoma ši informacija: pavadinimas; 
# darbuotojų kiekis; adresas; praeitos savaitės iškeptų kepinių kiekiai 
# (sąrašas su 7-iais elementais, kur nurodyti atskiri kepinių kiekiai). 
# Susikurkite dictionaries kiekvienai kepyklai. Jeigu vienas kepinys parduodamas už 1.5 euro, 
# raskite kuri kepykla galėjo būti pelningiausia. Taip pat, išsiaiškinkite kiek vidutiniškai kiekviena 
# kepykla per dieną pagamina kepinių, raskite kurios kepyklos vidurkis mažiausias.

kepykla1 = {
    "pavadinimas" : "Bandeliu pasaulys",
    "darbuotoju kiekis" : 4,
    "adresas" : "jonausko g. 34",
    "praeitos savaites iskeptu kepiniu kiekiai" : 18,
    "prekes" : [2, 4, 6, 8]
}

kepykla2 = {
    "pavadinimas" : "Super pyragas",
    "darbuotoju kiekis" : 2,
    "adresas" : "saules g. 12-2",
    "praeitos savaites iskeptu kepiniu kiekiai" : 9,
    "prekes" : [1, 2, 3, 4,]
}

kepykla3 = {
    "pavadinimas" : "Iskepele",
    "darbuotoju kiekis" : 10,
    "adresas" : "visu krastu g. 9",
    "praeitos savaites iskeptu kepiniu kiekiai" : 24,
    "prekes" : [8, 9, 11, 5]
}
praeita_sav1 = kepykla1["praeitos savaites iskeptu kepiniu kiekiai"] * 1.5
db_sav1 = sum(kepykla1["prekes"])
praeita_sav2 = kepykla2["praeitos savaites iskeptu kepiniu kiekiai"] * 1.5
db_sav2 = sum(kepykla2["prekes"])
praeita_sav3 = kepykla3["praeitos savaites iskeptu kepiniu kiekiai"] * 1.5
db_sav3 = sum(kepykla3["prekes"])

if praeita_sav1 > praeita_sav2 and praeita_sav1 > praeita_sav3:
    print("Praeita savaite pelningiausia buvo kepykla:", kepykla1["pavadinimas"])
elif praeita_sav1 < praeita_sav2 and praeita_sav2 > praeita_sav3:
    print("Praeita savaite pelningiausia buvo kepykla:", kepykla2["pavadinimas"])
elif praeita_sav1 < praeita_sav3 and praeita_sav2 < praeita_sav3:
    print("Praeita savaite pelningiausia buvo kepykla:", kepykla3["pavadinimas"])

vid1 = kepykla1["praeitos savaites iskeptu kepiniu kiekiai"] / 5
vid2 = kepykla2["praeitos savaites iskeptu kepiniu kiekiai"] / 5
vid3 = kepykla3["praeitos savaites iskeptu kepiniu kiekiai"] / 5

if vid1 < vid2 and vid1 < vid3:
    print("Maziausiai kepiniu kepa kepykla:", kepykla1["pavadinimas"])
elif vid1 > vid2 and vid2 < vid3:
    print("Maziausiai kepiniu kepa kepykla:", kepykla2["pavadinimas"])
elif vid1 > vid3 and vid2 > vid3:
    print("Maziausiai kepiniu kepa kepykla:", kepykla3["pavadinimas"])
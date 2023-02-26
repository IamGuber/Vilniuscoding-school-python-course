# Susikurkite dictionary darbuotojo informacijai saugoti. 
# Nurodykite tokias savybes: vardas ir pavardė, telefonas, profesija, etatas, atlyginimas. 
# Taip pat, sukurkite dar vieną darbuotojo dictionary, tačiau nenurodykite 1-os ar 2-ų savybių, pvz, 
# praleiskite profesiją. Parašykite tokią programą, kuri galėtų išsiaiškinti kurios(-ių) savybių nėra antrame dictionary, 
# kurios yra pirmame, pvz jeigu nėra profesijos, tai programa išsiaiškintų, kad nėra nurodyta profesija antrame dictionary. 
# Padarykite taip, kad vartotojas turėtų galimybę suvesti trūkstamas savybes.

info = {
    "vardas" : "Jonas",
    "pavarde" : "Jonauskas",
    "telefonas" : 866666666,
    "profesija" : "Policijos patrulis",
    "etatas" : 1,
    "atlyginimas" : 1000,
}

info2 = {
    "vardas" : "Povilas",
    "pavarde" : "Povilauskas",
    "telefonas" : 868888888,
    "etatas" : 0.75,
    "atlyginimas" : 1200,
}

tuscias = []
for i in info:
    tuscias.append(i)
print(tuscias)

tuscias2 = []
for i in info2:
    tuscias2.append(i)
print(tuscias2)

trukumas = [x for x in tuscias + tuscias2 if x not in tuscias2]
if not trukumas:
    print("Darbuotoju keysai vienodi.")
else:
    print("Antram darbuotojui truksta keyso:", trukumas)

trukumas2 = [x for x in tuscias + tuscias2 if x not in tuscias]
if True in trukumas2:
    print("Pirmam darbuotojui truksta keyso:", trukumas2)

klausymas1 = int(input("Kuriam darbuotojui norite papildyti keysa? 1 ar 2?: "))
if klausymas1 == 2:
    prideti_keysa = input("Koki keysa norite prideti? ")
    prideti_value = input("Kokia savybe norite parasyti? ")
    info2[prideti_keysa] = prideti_value
elif klausymas1 == 1:
    prideti_keysa = input("Koki keysa norite prideti? ")
    prideti_value = input("Kokia savybe norite parasyti? ")
    info[prideti_keysa] = prideti_value

print(info)
print()
print(info2)
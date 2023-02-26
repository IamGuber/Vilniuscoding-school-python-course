# Susikurkite studento pažymių sąrašą ir užpildykite jį duomenimis (atsitiktiniais arba kokius įrašysite). 
# Išveskite kiekvieną pažymį atskiroje eilutėje. Prie kiekvieno pažymio nurodykite ar tai teigiamas, ar neigiamas pažymys. 
# Taip pat, jeigu neigiamas pažymys, tuomet dar nurodykite kiek balų trūko iki teigiamo pažymio. Teigiamas pažymys skaitosi 5 balai.

pazymiai = list(range(2, 11))

for i in pazymiai:
    if i >= 5:
        print("Pazymys", i, "tegiamas.")
    elif i < 5:
        for x in range(2, 4):
            if i + x == 5:
                print("Pazymys", i, "neigiamas. Iki teigiamo pazymio pritruko", x, "balu.")
            if i + 1 == 5:
                print("Pazymys", i, "neigiamas. Iki teigiamo pazymio pritruko 1 balo.")
                break
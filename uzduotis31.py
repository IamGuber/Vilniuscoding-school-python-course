# Susikurkite pažymių sąrašą. Šiuos pažymius leiskite įvesti vartotojui. 
# Baigus įvedimą, išveskite suvestų pažymių vidurkį. 
# Taip pat, jeigu studentas turėjo neigiamų pažymių, tuomet atskirai parodykite tuos neigiamus pažymius ir jų kiekį.

pazymiai = []
neigiami_paz = []
kiekis = 0
ivedimas = 0

kiekis = int(input("Iveskite kiek norite ivesti pazymiu: "))

while kiekis > ivedimas:
    ivestis = int(input("Iveskite pazymi: "))
    ivedimas += 1
    pazymiai.append(ivestis)

for i in pazymiai:
    if i < 4:
        neigiami_paz.append(i)

vidurkis = round(sum(pazymiai) / ivedimas, 2) 
print("Pazymiu vidurkis:", vidurkis)
print("Neigami pazymiai:", neigiami_paz)
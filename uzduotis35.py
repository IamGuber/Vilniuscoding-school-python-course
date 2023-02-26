# Susikurkite dviejų studentų pažymių sąrašus. Šią informaciją leiskite suvesti vartotojui. 
# Raskite kurio studento vidurkis yra geresnis. Taip pat, ar kuris iš jų (ar abu) turi neigiamų pažymių.

student1 = []
student2 = []

pazymiai_pirmo = 0
neigiami_pirmo = 0
pazymiai_antro = 0
neigiami_antro = 0

kiekis_pirmo = int(input("Iveskite kiek pazymiu turi pirmas studentas: "))
while pazymiai_pirmo < kiekis_pirmo:
    pazymys = int(input("Iveskite pazymi: "))
    pazymiai_pirmo += 1
    student1.append(pazymys)
    if pazymys < 5:
        neigiami_pirmo += 1

kiekis_antro = int(input("Iveskite kiek pazymiu turi antras studentas: "))
while pazymiai_antro < kiekis_antro:
    pazymys = int(input("Iveskite pazymi: "))
    pazymiai_antro += 1
    student2.append(pazymys)
    if pazymys < 5:
        neigiami_antro += 1

pirmo_stud_vidurkis = round(sum(student1) / len(student1), 2)
antro_stud_vidurkis = round(sum(student2) / len(student2), 2)

if pirmo_stud_vidurkis > antro_stud_vidurkis:
    print("Pirmo studento vidurkis yra geresnis nei antro.")
    print("Pirmo studento vidurkis:", pirmo_stud_vidurkis)
    print("Antro studento vidurkis:", antro_stud_vidurkis)
elif antro_stud_vidurkis > pirmo_stud_vidurkis:
    print("Antro studento vidurkis yra geresnis nei pirmo.")
    print("Antro studento vidurkis:", antro_stud_vidurkis)
    print("Pirmo studento vidurkis:", pirmo_stud_vidurkis)
else:
    print("Studentai turi vienodus vidurkius.")

if neigiami_pirmo > 0:
    print("Pirmas studentas turi", neigiami_pirmo, "neigiama'ius pazymi'us")
if neigiami_antro > 0:
    print("Antraas studentas turi", neigiami_antro, "neigiama'ius pazymi'us")
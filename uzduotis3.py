# Leiskite vartotojui suvesti norimą kiekį pažymių (pavyzdžiui, jūs nusimatote 3-is kintamuosius, tai leidžiate padaryti 3 įvedimus). Raskite šių pažymių vidurkį. Patikrinkite ar vidurkis teigiamas (daugiau arba lygu 5-iems), jei taip - išveskite "vidurkis teigiamas".

print("Iveskite(per ENTER) keturius pazymius:")

pz1 = int(input())
pz2 = int(input())
pz3 = int(input())
pz4 = int(input())

vidurkis = (pz1 + pz2 + pz3 + pz4) / 4

if vidurkis >= 5:
    print("Vidurkis teigiamas:", vidurkis)
if vidurkis < 5:
    print("Vidurkis neigiamas:", vidurkis)
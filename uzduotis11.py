# Susikurkite tris skaičius arba leiskite visus skaičius suvesti vartotojui. Tikrinkite (naudojant visas if sąlygos dalis):
# Ar pirmi du skaičiai lygūs?
# Ar pirmas ir trečias skaičiai lygūs?
# Ar trečias skaičius didesnis už pirmą?
# Ar antras skaičius lygus dvigubai trečio skaičiaus reikšmei?
# Ar pirmas skaičius dalinasi iš 3?
# Jei nieko nepavyko rasti, išveskite klaidos pranešimą.

skc1 = int(input("Iveskite pirma skaiciu: "))
skc2 = int(input("Iveskite antra skaiciu: "))
skc3 = int(input("Iveskite trecia skaiciu: "))

if skc1 == skc2:
    print("Pirmi du skaiciai yra lygus.")
elif skc1 == skc3:
    print("Pirmas ir trecias skaiciai yra lygus.")
elif skc3 > skc1:
    print("Trecias skaicius yra didesnis uz pirma.")
elif skc2 == skc3 * 2:
    print("Antras skaicius lygus dvigubai trecio skaiciaus reiksmei.")
elif skc1 % 3 == 0:
    print("Pirmas skaicius dalinas is 3.")
else:
    print("Ivestu skaiciu klaida.")
# Susikurkite tris skaičių kintamuosius su norimomis reikšmėmis, arba leiskite šiuos skaičius suvesti vartotojui. Patikrinkite šias sąlygas (naudojant elif dalis):
# Ar pirmas skaičius didesnis už antrą?
# Ar antras skaičius didesnis už trečią?
# Ar trečias skaičius didesnis už pirmą?
# Ar pirmi du skaičiai yra lygūs?
# Ar paskutiniai du skaičiai yra lygūs?
# Ar pirmas skaičius yra lygus 0?
# Ar antras skaičius neigiamas?
# Ar trečias skaičius teigiamas?

print("Iveskite per ENTER trys skaicius:")
skc1 = int(input())
skc2 = int(input())
skc3 = int(input())

if skc1 > skc2:
    print("Pirmas skaicius didesnis uz antra.")
elif skc2 > skc3:
    print("Antras skaicius didesnis uz trecia.")
elif skc3 > skc1:
    print("Trecias skaicius didesnis uz pirma.")
elif skc1 == skc2:
    print("Pirmi du skaicia yra lygus.")
elif skc2 == skc3:
    print("Paskutini du skaiciai yra lygus.")
elif skc1 == 0:
    print("Pirmas skaicius yra lygus nuliui.")
elif skc2 < 0:
    print("Antras skaicius yra neigiamas.")
elif skc3 > 0:
    print("Trecias skaicius yra teigiamas")
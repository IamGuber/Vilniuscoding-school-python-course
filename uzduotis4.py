# Susikurkite skaičiaus kintamąjį arba leiskite šį skaičių įvesti vartotojui. Atlikite šiuos patikrinimus ir veiksmus:
# Jei skaičius dalinasi iš 5, tuomet išveskite šio skaičiaus daugybos lentelę nuo 1 iki 5.
# Jei skaičius lyginis, tuomet išveskite šį skaičių, jo kvadratą ir jį padalintą iš 2.
# Jei skaičius nesidalina iš 7, tuomet susikurkite antrąjį kintamąjį, išveskite šių dviejų skaičių sumą, skirtumą, sandaugą, dalmenį.

skaicius = int(input("Iveskite viena skaiciu:"))

if skaicius % 5 == 0:
    x = range(1, 5)
    for y in x:
        print("Daugybos lentele is skaiciaus, nuo 1 iki 5:", skaicius * y)
print()
if skaicius % 2 == 0:
    print("Skacius:", skaicius,)
    print("Skaiciaus kvadratas padalintas is dvieju:", (skaicius ** 2) / 2)
print()
if skaicius % 7 > 0:
    new_number = 6
    print("Ivesto skaiciaus ir naujo skaiciaus suma:", skaicius + new_number)
    print("Ivesto skaiciaus ir naujo skaiciaus skirtumas:", skaicius - new_number)
    print("Ivesto skaiciaus ir naujo skaiciaus sandauga:", skaicius * new_number)
    print("Ivesto skaiciaus ir naujo skaiciaus dalmuo:", skaicius / new_number)
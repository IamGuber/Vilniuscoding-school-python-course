# Susikurkite skaičiui saugoti skirtą kintamąjį, arba reikšmę leiskite suvesti vartotojui. Tikrinkite (naudojant visas if sąlygos dalis):
# Ar skaičius yra lyginis?
# Ar dalinasi iš 5?
# Ar skaičius lygus 3?
# Jeigu nieko nepavyko rasti, išveskite klaidos pranešimą.

skc = int(input())

if skc % 2 == 0:
    print("Skaicius yra lyginis.")
elif skc % 5 == 0:
    print("Skaicius dalinas is 5.")
elif skc == 3:
    print("Skaicius lygus 3.")
else:
    print("Skacius nesutampa.")
# Susikurkite kintamąjį egzamino pažymiui saugoti [0-10]. Naudojant elif dalis patikrinkite šias sąlygas ir išveskite atitinkamą tekstą:
# Jei pažymys yra lygus 10 išvesti “puiku”.
# Jei pažymys yra lygus arba didesnis nei 9 išvesti “labai gerai”.
# Jei pažymys yra lygus arba didesnis nei 7 išvesti “gerai”.
# Jei pažymys yra lygus arba didesnis nei 5 išvesti “patenkinamai”.
# Jei pažymys mažesnis nei 5 išvesti “egzaminas neišlaikytas”.

pazymys = int(input())

if pazymys == 10:
    print("Puiku!")
elif pazymys >= 9:
    print("Labai gerai!")
elif pazymys >= 7:
    print("Gerai!")
elif pazymys >= 5:
    print("Patenkinamai!")
elif pazymys < 5:
    print("Egzaminas neislaikytas!")
# Leiskite vartotojui suvesti norimą skaičių. Patikrinkite ar šis skaičius dalinasi iš 7, jei taip išveskite vieną tekstą, jei ne - kitą.

skc = int(input())

if skc % 7 == 0:
    print("Skaicius dalinasi is 7.")
else:
    print("Skaicius nesidalina is 7.")
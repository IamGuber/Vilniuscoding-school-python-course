# Susikurkite trijų egzaminų rezultatų kintamuosius arba paprašykite, kad vartotojas suvestų šias reikšmes. Suraskite pažymių vidurkį. Atlikite šiuos patikrinimus:
# ar gautas vidurkis yra [8-10];
# ar gautas vidurkis yra [5-8);
# ar gautas vidurkis yra < 5.

skc1 = int(input("Iveskite pirma skaiciu: "))
skc2 = int(input("Iveskite antra skaiciu: "))
skc3 = int(input("Iveskite trecia skaiciu: "))

vidurkis = (skc1 + skc2 + skc3) / 3

if vidurkis >= 8 or vidurkis == 10:
    print("Vidurkis nuo 8 iki 10")
elif vidurkis >= 5 or vidurkis == 8:
    print("Vidurkis nuo 5 iki 8")
elif vidurkis < 5:
    print("Vidurkis maziau nei 5")
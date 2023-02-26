# Išveskite visus skaičius nuo 1 iki kol pasitaikys toks, kuris yra pirminis ir yra didesnis nei 20.

skc2 = 1

while skc2 < 100:
    skc2 += 1
    print(skc2)
    if skc2 % 2 != 0 and skc2 % 3 != 0 and skc2 % skc2 == 0 and skc2 > 20:
        print(skc2, "skaicius yra pirminis ir didesnis nei 20.")
        break
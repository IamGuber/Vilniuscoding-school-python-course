# Susikurkite programą, kurioje būtų sukurtas sąrašas iš pasirinkto kiekio atsitiktinių skaičių. 
# Raskite kiekvieno skaičiaus daliklius, pavyzdžiui:
# skaičius 2 dalinasi iš 2
# skaičius 3 dalinasi iš 3
# skaičius 4 dalinasi iš 2, 4
# skaičius 5 dalinasi iš 5
# skaičius 6 dalinasi iš 2, 3, 6

import random

sarasas = []

print("Iveskite kiek norite sugeneruoti nuo 1 iki 100 atsitiktiniu skaiciu:")
skc = int(input())

for i in range(skc):
    sarasas.append(random.randint(1, 100))

print("Sugeneruoti skaiciai:", sarasas)

for skaicius in sarasas:
    tuscias = []
    for x in range(2, 10):
        if skaicius % x == 0:
            tuscias.append(x)
    if len(tuscias) == 0:
        continue
    redaguotas = ", ".join(str(skc) for skc in tuscias)
    print("Skaicius", skaicius, "dalinasi is", redaguotas)
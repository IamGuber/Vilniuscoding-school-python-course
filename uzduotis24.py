# Susikurkite programą, kurioje vartotojas galėtų nusakyti kiek atsitiktinių skaičių turėtų būti sugeneruota. 
# Tuomet programa turėtų būtent tokį kiekį atsitiktinių skaičių sugeneruoti ir sudėti į sąrašą. Išveskite visus šiuos skaičius ekrane. 
# Tuomet tuos pačius skaičius išveskite ekrane dar kartą, tačiau viską spausdinkite atskirose eilutėse, 
# eilutėje nurodant patį skaičių ir jo kvadratą.

import random

sarasas = []

skaiciai = int(input("Iveskite kiek skaiciu norite sugeneruoti: "))

for skaicius in range(skaiciai):
    sarasas.append(random.randint(0, 100))

print(sarasas)

for eiles in sarasas:
    print(eiles, "skaiciaus kvadratas:", eiles**2)
# Susikurkite funkciją, kuri per argumentus priimtų skaičių masyvą. 
# Funkcija turėtų rasti didžiausią skaičių iš masyvo bei išvesti gautą atsakymus. 
# Taip pat, susikurkite funkciją, kuri per argumentus priimtų masyvą ir į jį sugeneruotų pasirinktą kiekį atsitiktinių skaičių. 
# Susikurkite tris tuščius masyvus. Iškvieskite atsitiktinių skaičių generavimo funkciją tris kartus, 
# kiekvieną kartą perduodant funkcijai vis kitą masyvą. Kai duomenys bus užpildyti, 
# masyvuose esančią informaciją išsiveskite norimu būdu (per console.log arba per dar atskirą funkciją). 
# Tuomet kvieskite didžiausio skaičiaus paieškos funkciją tris kartus, kiekvieną kartą perduodant skirtingą masyvą į ją.

import random

def did_skc(skc_masyvas):
    max = skc_masyvas[0]
    for i in skc_masyvas:
        if i > max:
            max = i
    print("Didziausias skaicius is saraso:", max)


sarasas1 = []
sarasas2 = []
sarasas3 = []

def nauj_sar(kiekis, sarasas):
    for i in range(kiekis):
        sarasas.append(random.randint(1, 100))
    print(f"Sarasas: {sarasas}")
    did_skc(sarasas)
    print()


nauj_sar(10, sarasas1)
nauj_sar(5, sarasas2)
nauj_sar(15, sarasas3)
# Susikurkite bent 3 matematines funkcijas, priimančias reikiamus argumentus 
# (pvz suma iš dviejų skaičių, suma iš trijų skaičių, skirtumas, sandauga, dalyba) ir grąžinančias atitinkamus atsakymus. 
# Taip pat, susikurkite funkciją, kurioje būtų sugeneruojamas reikiamas kiekis atsitiktinių skaičių ir išvedami 
# visų skaičiavimų atsakymai su veiksmais (iškviečiant atitinkamas kitas funkcijas ir perduodant reikiamus kintamuosius) 
# (pagal 23 pavyzdį). Iškvieskite šią pagrindinę funkciją bent kartą.

from random import randint


def suma(skc1, skc2, skc3):
    return skc1 + skc2 + skc3


def skirtumas(skc1, skc2):
    return skc1 - skc2


def sandauga(skc1, skc2):
    return skc1 * skc2


def skaiciai():
    skc1 = randint(1, 10)
    skc2 = randint(1, 10)
    skc3 = randint(1, 10)
    return f"Suma: {skc1} + {skc2} + {skc3} = {suma(skc1, skc2, skc3)}\nSkirtumas: {skc1} - {skc2} = {skirtumas(skc1, skc2)}\nSandauga: {skc1} * {skc2} = {sandauga(skc1, skc2)}"


print(skaiciai())
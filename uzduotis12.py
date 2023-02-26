# Sukurkite funkciją sumai skaičiuoti, ši funkcija per argumentus turėtų gauti du skaičius, 
# bei išvesti patį veiksmą kartu su atsakymu (pvz 7 + 5 = 12). Sukurkite tokias pačias funkcijas skirtumui, 
# sandaugai ir dalmeniui rasti. Sukurkite dar vieną funkciją, kuri sugeneruotų du atsitiktinius skaičius, 
# bei iškviestų kitas 4 funkcijas, perduodant joms sugeneruotus skaičius. Šią bendrąją funkciją iškvieskite keletą kartų.

import random

def suma(skc1, skc2):
    print(f"{skc1} + {skc2} = {skc1 + skc2}")


def skirtumas(skc1, skc2):
    print(f"{skc1} - {skc2} = {skc1 - skc2}")


def sandauga(skc1, skc2):
    print(f"{skc1} * {skc2} = {skc1 * skc2}")


def dalmuo(skc1, skc2):
    print(f"{skc1} / {skc2} = {skc1 / skc2}")


def skaiciai():
    skc1 = random.randint(1, 10)
    skc2 = random.randint(1, 10)
    suma(skc1, skc2)
    skirtumas(skc1,skc2)
    sandauga(skc1, skc2)
    dalmuo(skc1, skc2)
    print()


skaiciai()
skaiciai()
skaiciai()
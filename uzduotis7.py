# Sukurkite funkciją, kuri išvestų 10 atsitiktinių skaičių. Po visų išvestų skaičių turėtų padėti tuščią eilutę. Šią funkciją iškvieskite 5 kartus.

import random

def info():
    for skaicius in range(10):
        skaicius = random.randint(1, 100)
        print(skaicius, "\n")

info()
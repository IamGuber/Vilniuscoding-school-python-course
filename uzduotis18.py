# Susikurkite funkciją, kuri grąžintų atsitiktinai sugeneruotą skaičių. 
# Iškvieskite šią funkciją kelis kartus ir gautus atsakymus išveskite kokiu norite būdu.

import random


def info():
    return random.randint(1, 100)

print("Pirmas atsitiktinis skaicius: ", info())
print("Antras atsitiktinis skaicius: ", info())
print("Trecias atsitiktinis skaicius: ", info())
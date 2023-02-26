# Susikurkite funkciją, kuri per argumentus gautų skaičių. Ji turėtų surasti duoto skaičiaus mažiausią daliklį 
# (skaičių iš kurio dalinasi be liekanos). Už funkcijos ribų sukite ciklą nuo 10 iki 30 ir kiekvienoje 
# ciklo iteracijoje iškvieskite šią funkciją, perduodant ciklo kintamąjį.


def info(skaicius):
    for i in range(2, 100):
        if skaicius % i == 0:
            return f"Skaicius {skaicius} maziausias daliklis yra: {i}"
        else: 
            continue


for x in range(10, 30):
    print(info(x))
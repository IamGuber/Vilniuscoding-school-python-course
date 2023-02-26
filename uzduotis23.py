# Susikurkite funkciją kuri priimtų skaičių masyvą per argumentus. Ši funkcija turėtų rasti duotųjų skaičių sumą ir grąžinti gautą atsakymą. 
# Už funkcijos ribų susikurkite du skaičių masyvus ir užpildykite juos duomenimis. 
# Iškvieskite turimą funkciją du kartus, jai abu kartus perduodant skirtingą masyvą. Gautus atsakymus išveskite. 
# Taip pat, raskite kuri suma gavosi didesnė ir išveskite atsakymą.


def info(masyvas):
    suma = 0
    for i in masyvas:
        suma += i
    return suma


sarasas1 = [22, 2, 33, 3, 44, 4]
sarasas2 = [12, 2, 31, 1, 51, 5]

print(info(sarasas1))
print()
print(info(sarasas2))

suma1 = sum(sarasas1)
suma2 = sum(sarasas2)
if suma1 > suma2:
    print("Pirmo saraso skaiciu suma yra didesne uz antro.")
elif suma1 < suma2:
    print("Antro saraso skaiciu suma yra didesne uz pirmo.")
else:
    print("Abieju sarasu skaiciu suma yra vienoda.")
# Susikurkite funkciją, kuri per argumentus priimtų skaičių masyvą. 
# Funkcija turėtų atspausdinti visus skaičius, šalia jų išvedant to skaičiaus kvadratą ir jį padalintą iš dviejų. 
# Už funkcijos ribų susikurkite du skaičių masyvus ir užpildykite jį duomenimis. 
# Iškvieskite funkciją du kartus, kiekvieną kartą perduodant skirtingą turimą masyvą.

def info(skc_masyvas):
    for i in skc_masyvas:
        print(f"{i} sio skaiciaus kvadras yra {i * i}. Skaicius {i} padalintas is 2: {i / 2}")


sarasas1 = [1, 12, 2, 22, 3, 33]
sarasas2 = [2, 32, 3, 31, 5, 44]

info(sarasas1)
print()
info(sarasas2)
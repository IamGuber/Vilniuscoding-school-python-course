# Susikurkite funkciją kuri per argumentus priimtų žodžių masyvą. Ji turėtų rasti ir grąžinti ilgiausią žodį masyve. 
# Už funkcijos ribų susikurkite žodžių masyvą. Iškvieskite funkciją perduodant jai žodžių masyvą. 
# Gautą atsakymą išveskite, taip pat, nurodykite šio žodžio ilgį.


def info(masyvas):
    ilgiausias_zodis = masyvas[0]
    for i in masyvas:
        if len(i) > len(ilgiausias_zodis):
            ilgiausias_zodis = i
    return f"Ilgiausias zodis sarase yra: {ilgiausias_zodis}"


sarasas = ["pirmas", "antras", "trecias", "ketvirtas", "penktas"]

print(info(sarasas))
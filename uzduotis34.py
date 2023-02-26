# Susikurkite žodžių masyvą. Išveskite per kiek simbolių yra ilgesnis ilgiausias žodis už trumpiausią. 
# Tarkime ilgiausias yra “kompiuteris” (11 simbolių), o trumpiausias “medis” (5), skirtumas tarp jų 11 - 5 = 6 simboliai.

sarasas = ["pirmas", "antras", "trecias", "ketvirtas", "penktas"]
ilgiausias = sarasas[0]
trumpiausias = sarasas[0]

for i in sarasas:
    if len(i) > len(ilgiausias):
        ilgiausias = i
    elif len(i) < len(trumpiausias):
        trumpiausias = i

print(ilgiausias, "zodis turi: ", len(ilgiausias), "simboliu.")
print(trumpiausias, "zodis turi: ", len(trumpiausias), "simboliu.")
print("Skirtumas tarp ju:", len(ilgiausias), "-", len(trumpiausias), "=", len(ilgiausias) - len(trumpiausias))
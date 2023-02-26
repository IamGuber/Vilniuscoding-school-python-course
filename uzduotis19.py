# Sukurkite norimą sąrašą iš dictionary elementų su norimais duomenimis. Atlikite išvedimus ir pasirinktus skaičiavimus.

sarasas = [
    {
        "kompiuteris" : "MSI",
        "procesorius" : 13100,
        "ram" : 64,
        "ssd" : 1000,
        "vaizdo plokste" : "RTX 4090",
        "pagaminimo metai" : 2021
    },
    {
        "kompiuteris" : "LENOVO",
        "procesorius" : 13100,
        "ram" : 32,
        "ssd" : 2000,
        "vaizdo plokste" : "RTX 3090",
        "pagaminimo metai" : 2020
    },
    {
        "kompiuteris" : "ACER",
        "procesorius" : 10500,
        "ram" : 16,
        "ssd" : 500,
        "vaizdo plokste" : "RTX 3060 TI",
        "pagaminimo metai" : 2016
    },
    {
        "kompiuteris" : "ASUS",
        "procesorius" : 12400,
        "ram" : 24,
        "ssd" : 1500,
        "vaizdo plokste" : "RTX 3070",
        "pagaminimo metai" : 2019
    }
]

for i in sarasas:
    print(i)
    metai = 2022 - i["pagaminimo metai"]
    print("Kompiuteriui", metai, "metai.")

if sarasas[0]["ram"] < sarasas[1]["ram"] and sarasas[0]["ram"] < sarasas[2]["ram"] and sarasas[0]["ram"] < sarasas[3]["ram"]:
    print("Maziausiai operatyvios atminties turi MSI kompiuteris.")
elif sarasas[0]["ram"] > sarasas[1]["ram"] and sarasas[1]["ram"] < sarasas[2]["ram"] and sarasas[1]["ram"] < sarasas[3]["ram"]:
    print("Maziausiai operatyvios atminties turi LENOVO kompiuteris.")
elif sarasas[0]["ram"] > sarasas[2]["ram"] and sarasas[1]["ram"] > sarasas[2]["ram"] and sarasas[2]["ram"] < sarasas[3]["ram"]:
    print("Maziausiai operatyvios atminties turi ACER kompiuteris.")
elif sarasas[0]["ram"] > sarasas[3]["ram"] and sarasas[1]["ram"] > sarasas[3]["ram"] and sarasas[2]["ram"] > sarasas[3]["ram"]:
    print("Maziausiai operatyvios atminties turi ASUS kompiuteris.")

if sarasas[0]["ram"] > sarasas[1]["ram"] and sarasas[0]["ram"] > sarasas[2]["ram"] and sarasas[0]["ram"] > sarasas[3]["ram"]:
    print("Daugiausiai operatyvios atminties turi MSI kompiuteris.")
elif sarasas[0]["ram"] < sarasas[1]["ram"] and sarasas[1]["ram"] > sarasas[2]["ram"] and sarasas[1]["ram"] > sarasas[3]["ram"]:
    print("Daugiausiai operatyvios atminties turi LENOVO kompiuteris.")
elif sarasas[0]["ram"] < sarasas[2]["ram"] and sarasas[1]["ram"] < sarasas[2]["ram"] and sarasas[2]["ram"] > sarasas[3]["ram"]:
    print("Daugiausiai operatyvios atminties turi ACER kompiuteris.")
elif sarasas[0]["ram"] < sarasas[3]["ram"] and sarasas[1]["ram"] < sarasas[3]["ram"] and sarasas[2]["ram"] < sarasas[3]["ram"]:
    print("Daugiausiai operatyvios atminties turi ASUS kompiuteris.")

ssd = 0
visi_ssd = 0
while ssd != 4:
    for y in sarasas:
        ssd += 1
        visi_ssd += y["ssd"]
vid_ssd = visi_ssd / len(sarasas)
print("Vidutine talpa visu kompiuteriu SSD atminties disku yra", vid_ssd, "GB.")
print("Suma visu kompiuteriu GB:", visi_ssd)
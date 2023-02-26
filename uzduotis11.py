# Sukurkite funkciją, kuri per argumentus gautų automobilių duomenis (markė, modelis, gamybos metai, darbinis tūris). 
# Ši funkcija turėtų šiuos duomenis išvesti kaip nors gražiai formatuotai. Iškvieskite šią funkciją du kartus, perduodant skirtingus duomenis jai.

def info(marke, modelis, gamybos_metai, darbinis_turis):
    print(f"Automobilis {marke} {modelis}, pagamintas {gamybos_metai} metais. Sis automobilis turi varikli {darbinis_turis} turio.")

info("Mercedes-Benz", "S-class", 2020, 3.2)
info("BMW", 7, 2015, 3.0)
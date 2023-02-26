# Susikurkite duomenų failą, iš kurio nusiskaitytumėte informaciją apie automobilius. 
# Išskaičiuokite keletą norimų dalykų (pvz. metų vidurkį) ir skaičiavimų rezultatus išveskite rezultatų faile.

with open("/Users/guber/Desktop/python mokymai/19-darbas-su-failais/automobiliai.txt", "r+") as autofailas:
    autofailas.read()
    vidurkis = (2020 + 2018 + 2022) / 3
    vidurkis = str(vidurkis)[:-2]
    vidurkis = int(vidurkis) # grazinam int jeigu reikes su metais dar kazka daryti
    
sarasas = []
with open("/Users/guber/Desktop/python mokymai/19-darbas-su-failais/automobiliai.txt") as autofailas:
    for eile in autofailas:
        eile = eile.rstrip("\n")
        isskaidyta = eile.split(";")
        auto = dict(
            Marke = isskaidyta[0],
            Gamybos_metai = isskaidyta[1],
            Darbinis_turis = isskaidyta[2],
            Sedimos_vietos = isskaidyta[3]
        )
        sarasas.append(auto)
    
with open("/Users/guber/Desktop/python mokymai/19-darbas-su-failais/automobiliai.txt", "a") as autofailas:
    if sarasas[0]["Darbinis_turis"] > sarasas[1]["Darbinis_turis"] and sarasas[0]["Darbinis_turis"] > sarasas[2]["Darbinis_turis"]:
        autofailas.write(f"\n{sarasas[0]['Marke']} turi didziausia variklio turi.")
    elif sarasas[0]["Darbinis_turis"] < sarasas[1]["Darbinis_turis"] and sarasas[1]["Darbinis_turis"] > sarasas[2]["Darbinis_turis"]:
        autofailas.write(f"\n{sarasas[1]['Marke']} turi didziausia variklio turi.")
    elif sarasas[0]["Darbinis_turis"] < sarasas[2]["Darbinis_turis"] and sarasas[1]["Darbinis_turis"] < sarasas[2]["Darbinis_turis"]:
        autofailas.write(f"\n{sarasas[2]['Marke']} turi didziausia variklio turi.")

    if sarasas[0]["Darbinis_turis"] < sarasas[1]["Darbinis_turis"] and sarasas[0]["Darbinis_turis"] < sarasas[2]["Darbinis_turis"]:
        autofailas.write(f"\n{sarasas[0]['Marke']} turi maziausia variklio turi.")
    elif sarasas[0]["Darbinis_turis"] > sarasas[1]["Darbinis_turis"] and sarasas[1]["Darbinis_turis"] < sarasas[2]["Darbinis_turis"]:
        autofailas.write(f"\n{sarasas[1]['Marke']} turi maziausia variklio turi.")
    elif sarasas[0]["Darbinis_turis"] > sarasas[2]["Darbinis_turis"] and sarasas[1]["Darbinis_turis"] > sarasas[2]["Darbinis_turis"]:
        autofailas.write(f"\n{sarasas[2]['Marke']} turi maziausia variklio turi.")
    autofailas.write(f"\nVisu auto gamybos metu vidurkis yra {vidurkis}m. \n")
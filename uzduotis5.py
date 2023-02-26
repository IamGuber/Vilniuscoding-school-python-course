# Pasikurkite kitą csv failą, su kitais duomenimis. Pamėginkite nuskaityti šį failą pasirinktu būdu. 
# Išsiskaičiuokite iš šio failo norimus dalykus. Išveskite pradinius duomenis ir gautus rezultatus.

from csv import reader, writer

with open("/Users/guber/Desktop/python mokymai/19-darbas-su-failais/prekes.csv") as failas:
    info = reader(failas)
    info = reader(failas, delimiter=",")

    prekiu_kiekis = 0
    for i in info:
        prekiu_kiekis += int(i[1])
        print(i)
    print("Is viso prekiu yra:", prekiu_kiekis)

with open("/Users/guber/Desktop/python mokymai/19-darbas-su-failais/prekes.csv", "a", newline="") as failas:
    naujas = writer(failas)
    naujas.writerow([])
    naujas.writerow(list(["Plansetai", "3"]))

with open("/Users/guber/Desktop/python mokymai/19-darbas-su-failais/prekes.csv") as failas:
    info = reader(failas)
    info = reader(failas, delimiter=",")

    prekiu_kiekis = 0
    for i in info:
        prekiu_kiekis += int(i[1])
        print(i)
    print("Is viso prekiu yra:", prekiu_kiekis)
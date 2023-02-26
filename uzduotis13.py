# Susikurkite funkciją, kuri per argumentus priimtų žodžių masyvą. 
# Funkcijoje išveskite visus žodžius iš masyvo atskirose eilutėse, nurodant žodžio ilgį (simbolių kiekį). 
# Už funkcijos ribų susikurkite žodžių masyvą ir užpildykite jį duomenimis. Iškvieskite sukurtą funkciją perduodant turimą masyvą.

def info(zodziu_masyvas):
    for i in zodziu_masyvas:
        print(i, "Simbliu kiekis:", len(i))


sarasas = ["Pienas", "Duona", "Arbata", "Kukuruza", "Bananas", "Alus"]
info(sarasas)
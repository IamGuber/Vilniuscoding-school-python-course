# Susikurkite funkciją, kuri per argumentus priimtų studento vardą ir vidurkį. 
# Ši funkcija turėtų sugeneruoti iš to sakinį (pvz Studentas Tomas turi vidurkį 8.7) ir tai grąžinti kaip atsakymą. 
# Iškvieskite šią funkciją bent porą kartų, perduodant vis skirtingus duomenis. Gautus atsakymus išveskite.


def info(vardas, vidurkis):
    return f"Studentas {vardas} turi vidurki {vidurkis}."


pirmas_studentas = "Jonas"
pirmo_vidurkis = 9.2
antras_studentas = "Povilas"
antro_vidurkis = 7.7
trecias_studentas = "Jokubas"
trecio_vidurkis = 8.9

print(info(pirmas_studentas, pirmo_vidurkis))
print(info(antras_studentas, antro_vidurkis))
print(info(trecias_studentas, trecio_vidurkis))
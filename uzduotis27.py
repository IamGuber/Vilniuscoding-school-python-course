# Susikurkite sąrašą ir jį užpildykite atsitiktiniais skaičiais. Išveskite visus skaičius didesnius nei vidurkis.

sarasas = [1, 12, 2, 23, 3, 34, 4, 45, 5, 56]

vidurkis = sum(sarasas) / len(sarasas)
vidurkis = round(vidurkis, 1)
print("Vidurkis:", vidurkis)
print("Visi skaiciai didesni uz vidurki:")

for i in sarasas:
    if i > vidurkis:
        print(i)
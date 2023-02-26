# Sukurkite studentų pažymių vidurkių skaičiuoklę (kaip pavyzdį galite naudoti 17-ą pavyzdį). 
# Tačiau tokia skaičiuoklė turėtų leisti skaičiuoti vidurkį ne tik iš vieno studento pažymių, 
# bet leistų pakartoti pažymių įvedimą ir vidurkio skaičiavimą ant tiek studentų kiek reikia.

studentai = int(input("Iveskite studentu kieki: "))
st_kiekis = 1

while st_kiekis <= studentai:
    print("Iveskite kiek pazymiu turi", st_kiekis, "studentas?")
    st_paz = int(input())
    pazymiu_kiekis = 0
    suma = 0
    for ciklas in range(0, st_paz):
        pazymys = int(input("Iveskite pazymi: "))
        pazymiu_kiekis += 1
        suma += pazymys
        vidurkis = suma / pazymiu_kiekis
        print(f"Studento", st_kiekis, "vidurkis:", vidurkis)
    st_kiekis += 1
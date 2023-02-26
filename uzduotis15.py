# Susikurkite funkciją, kuri per argumentus priimtų pažymių masyvą, bei studento vardą su pavarde. 
# Funkcija turėtų išvesti studento vardą ir pavardę, jo pažymius. Taip pat, suskaičiuoti vidurkį, bei jį išvesti. 
# Už funkcijos ribų susikurkite reikiamus kintamuosius ir masyvus, arba objektus studentų pažymiams saugoti ir užpildykite juos duomenimis. 
# Iškvieskite šią funkciją perduodant visus reikalingus duomenis.

def info(vardas, pavarde, masyvas):
    tekstas = ", ".join(map(str, masyvas))
    suma = sum(masyvas)
    kiekis = len(masyvas)
    vidurkis = suma / kiekis
    print(f"Studentas {vardas} {pavarde}, jo pazymiai: {tekstas}. Pazymiu vidurkis: {vidurkis}.")


pirmas_stud = "Jonas"
pirmo_pavarde = "Jonauskas"
pazymiai = [10, 9, 10, 8, 6]

info(pirmas_stud, pirmo_pavarde, pazymiai)
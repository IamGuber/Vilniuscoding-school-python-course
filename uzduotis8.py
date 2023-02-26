# Sukurkite sąrašą, kuriame būtų surašyti studentų pažymiai. 
# Galite padaryti taip, kad pasirinktą kiekį pažymių galėtų suvesti pats vartotojas. 
# Programa turi pasakyti kiek dešimtukų studentas turi.

sarasas = []
pazymiu_kiekis = int(input("Iveskite kiek norite ivesti studentui pazymiu: "))
suma = 0

while suma < pazymiu_kiekis:
    sarasas.append(int(input("Iveskite per Enter studento pazymius: ")))
    skaiciavimas = sarasas.count(10)
    suma += 1
print("Studentas turi is viso", skaiciavimas, "desimtuka'us.")
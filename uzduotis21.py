# Susikurkite masyvą šalių pavadinimams saugoti ir jį užpildykite duomenimis. 
# Išveskite šalių pavadinimus atskirose eilutėse, su prierašu "šalis" ir tada nurodant šalį iš masyvo.

salys = ("Lietuva", "Latvija", "Estija", "Lenkija", "Vokietija")

for indeks, sls in enumerate(salys, start = 1):
    print("Salis:", indeks, sls)
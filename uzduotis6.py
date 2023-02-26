# Susikurkite norimą csv failą su duomenimis. Nuskaitykite šį failą pasirinktu būdu. 
# Paskaičiuokite ar raskite iš šio failo duomenų bent 3 skirtingus dalykus 
# (geriausiai besimokantį studentą, aukščiausią studentą, mažiausią vidurkį, …). 
# Gautus rezultatus išveskite į atskirą failą (galite tiesiog txt failą).

with open("/Users/guber/Desktop/python mokymai/19-darbas-su-failais/Studentai2.csv") as failas:
    
    next(failas)
    info = list(failas)
    redag = [eilute.rstrip("\n") for eilute in info]
    redag2 = [eilute2.split(";") for eilute2 in redag]
    pirmas_stud = redag2[0]
    antras_stud = redag2[1]
    trecias_stud = redag2[2]
    
    if pirmas_stud[2] > antras_stud[2] and pirmas_stud[2] > trecias_stud[2]:
        with open("/Users/guber/Desktop/python mokymai/19-darbas-su-failais/studentai.txt", "a") as failas:
            failas.write(f"Ilgiausiai mokasi studentas'e {pirmas_stud[0]} {pirmas_stud[1]}")
            failas.write("\n")
    elif pirmas_stud[2] < antras_stud[2] and antras_stud[2] > trecias_stud[2]:
        with open("/Users/guber/Desktop/python mokymai/19-darbas-su-failais/studentai.txt", "a") as failas:
            failas.write(f"Ilgiausiai mokasi studentas'e {antras_stud[0]} {antras_stud[1]}")
            failas.write("\n")
    elif trecias_stud[2] > antras_stud[2] and pirmas_stud[2] < trecias_stud[2]:
        with open("/Users/guber/Desktop/python mokymai/19-darbas-su-failais/studentai.txt", "a") as failas:
            failas.write(f"Ilgiausiai mokasi studentas'e {trecias_stud[0]} {trecias_stud[1]}")
            failas.write("\n")

    new_pirmas_stud = list(pirmas_stud[3].split(","))
    new_antras_stud = list(antras_stud[3].split(","))
    new_trecias_stud = list(trecias_stud[3].split(","))

    suma1 = 0
    for i in new_pirmas_stud:
        suma1 += int(i)
    vidurkis1 = suma1 / len(new_pirmas_stud)
    with open("/Users/guber/Desktop/python mokymai/19-darbas-su-failais/studentai.txt", "a") as failas:
        failas.write(f"Vidurkis studento'es {pirmas_stud[0]} {pirmas_stud[1]} yra {round(vidurkis1, 2)}")
        failas.write("\n")

    suma2 = 0
    for i in new_antras_stud:
        suma2 += int(i)
    vidurkis2 = suma2 / len(new_antras_stud)
    with open("/Users/guber/Desktop/python mokymai/19-darbas-su-failais/studentai.txt", "a") as failas:
        failas.write(f"Vidurkis studento'es {antras_stud[0]} {antras_stud[1]} yra {round(vidurkis2, 2)}")
        failas.write("\n")

    suma3 = 0
    for i in new_trecias_stud:
        suma3 += int(i)
    vidurkis3 = suma3 / len(new_trecias_stud)
    with open("/Users/guber/Desktop/python mokymai/19-darbas-su-failais/studentai.txt", "a") as failas:
        failas.write(f"Vidurkis studento'es {trecias_stud[0]} {trecias_stud[1]} yra {round(vidurkis3, 2)}")
        failas.write("\n")

    if vidurkis1 > vidurkis2 and vidurkis1 > vidurkis3:
        with open("/Users/guber/Desktop/python mokymai/19-darbas-su-failais/studentai.txt", "a") as failas:
            failas.write(f"Geriausiai mokasi {pirmas_stud[1]}")
            failas.write("\n")
    elif vidurkis1 < vidurkis2 and vidurkis2 > vidurkis3:
        with open("/Users/guber/Desktop/python mokymai/19-darbas-su-failais/studentai.txt", "a") as failas:
            failas.write(f"Geriausiai mokasi {antras_stud[1]}")
            failas.write("\n")
    elif vidurkis3 > vidurkis2 and vidurkis1 < vidurkis3:
        with open("/Users/guber/Desktop/python mokymai/19-darbas-su-failais/studentai.txt", "a") as failas:
            failas.write(f"Geriausiai mokasi {trecias_stud[1]}")
            failas.write("\n")
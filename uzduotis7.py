# Susikurkite norimą csv failą su duomenimis. Nuskaitykite šio failo duomenis pasirinktu būdu. 
# Atfiltruokite duomenis pagal pasirinktą kriterijų (pvz, visus studentus, kurių vidurkis didesnis nei 8) 
# ir šiuos atfiltruotus duomenis išspausdinkite į atskirą csv failą.

with open("/Users/guber/Desktop/python mokymai/19-darbas-su-failais/Studentai2.csv") as failas:
    next(failas)
    info = list(failas)
    redag = [eilute.rstrip("\n") for eilute in info]
    redag2 = [eilute2.split(";") for eilute2 in redag]

    pirmas_stud = redag2[0]
    antras_stud = redag2[1]
    trecias_stud = redag2[2]

    new_pirmas_stud = list(pirmas_stud[3].split(","))
    new_antras_stud = list(antras_stud[3].split(","))
    new_trecias_stud = list(trecias_stud[3].split(","))

    suma1 = 0
    for i in new_pirmas_stud:
        suma1 += int(i)
    vidurkis1 = suma1 / len(new_pirmas_stud)
    print("Vidurkis studento'es", pirmas_stud[0], pirmas_stud[1], "yra", round(vidurkis1, 2))

    suma2 = 0
    for i in new_antras_stud:
        suma2 += int(i)
    vidurkis2 = suma2 / len(new_antras_stud)
    print("Vidurkis studento'es", antras_stud[0], antras_stud[1], "yra", round(vidurkis2, 2))

    suma3 = 0
    for i in new_trecias_stud:
        suma3 += int(i)
    vidurkis3 = suma3 / len(new_trecias_stud)
    print("Vidurkis studento'es", trecias_stud[0], trecias_stud[1], "yra", round(vidurkis3, 2))

    if vidurkis1 > 8:
        with open("/Users/guber/Desktop/python mokymai/19-darbas-su-failais/Studentai2-geriausi.csv", "a") as failas:
            failas.write(f"{pirmas_stud[0]} {pirmas_stud[1]} {round(vidurkis1, 2)}")
            failas.write("\n")
    if vidurkis2 > 8:
        with open("/Users/guber/Desktop/python mokymai/19-darbas-su-failais/Studentai2-geriausi.csv", "a") as failas:
            failas.write(f"{antras_stud[0]} {antras_stud[1]} {round(vidurkis2, 2)}")
            failas.write("\n")
    if vidurkis3 > 8:
        with open("/Users/guber/Desktop/python mokymai/19-darbas-su-failais/Studentai2-geriausi.csv", "a") as failas:
            failas.write(f"{trecias_stud[0]} {trecias_stud[1]} {round(vidurkis3, 2)}")
            failas.write("\n")
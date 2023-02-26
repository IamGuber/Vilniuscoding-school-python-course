from multiprocessing.sharedctypes import Value
import os
import csv

os.system("")

class style():
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    RESET = '\033[0m'

print(style.GREEN + "\ntoDoLISTAS\n")
print(style.RESET)

sarasas_meniu = ['Perziureti savo "toDoLISTA"', "Sukurti nauja kategorija", "Sukurti kategorijoje nauja uzuoti", "Redagavimas", 'Issaugoti "toDoLISTAS"']
sarasas_meniu2 = ["Perziureti kategorija", "Sukurti nauja kategorija", "Sukurti kategorijoje nauja uzduoti", "Redagavimas", 'Issaugoti "toDoLISTAS"']
sarasas_meniu3 = ["Istrinti visa sarasas", "Istrinti kategorija", "Istrinti uzduoti", "Grizti i pagrindini meniu"]
sarasas_meniu4 = ["Trinti viska", "Trinti pasirinkta"]

kategorijos = {
    "parduotuve" : ["batonas", "pienas"], 
    "automobilis" : ["ratai"],
    "siandien" : ["i servisa", "i parde"]
}

print(style.YELLOW + "MENIU")
print(style.RESET)
for i, x in enumerate(sarasas_meniu):
    print(f"{i + 1} - {x}")
print()


def trinimas_temos():
    print()
    for i in kategorijos:
        print(i)
    print()
    klausymas_del_trinimo = input(style.BLUE + "Pasirinkite is kokios kategorijos trinti uzduotys: " + style.RESET)
    if klausymas_del_trinimo in kategorijos:
        print()
        for x in kategorijos[klausymas_del_trinimo]:
            print(x)
        print()


        def trinimas_pasirinktu():
            print()
            for i2, x2 in enumerate(kategorijos[klausymas_del_trinimo]):
                print(f'{i2 + 1} - {x2}')
            print()
            try:
                temos_kiekio_trinimas = int(input(style.BLUE + "Kiek uzduociu norite istrinti? " + style.RESET))
                trinimai = 0
                if temos_kiekio_trinimas <= len(kategorijos[klausymas_del_trinimo]):
                    while trinimai < temos_kiekio_trinimas:
                        trinimai += 1
                        try:
                            temos_delete = int(input(style.BLUE + "Iveskite skaiciu, kokia uzduoti norite istrinti: " + style.RESET))
                            kategorijos[klausymas_del_trinimo].pop(temos_delete - 1)
                            print()
                            for i2, x2 in enumerate(kategorijos[klausymas_del_trinimo]):
                                print(f'{i2 + 1} - {x2}')
                            print()
                        except ValueError:
                            print()
                            print(style.RED + "Blogai ivedete skaiciu! Bandykite dar karta." + style.RESET)
                            trinimas_pasirinktu()
                    meniu_def()
                elif temos_kiekio_trinimas > len(kategorijos[klausymas_del_trinimo]):
                    temos_kiekio_trinimas2 = input(style.BLUE + "Ivedete daugiau arba tiek pat trinimu kiek yra uzduociu sarase. Gal norite istrinti viska? y/n\n" + style.RESET)
                    if temos_kiekio_trinimas2 == "y":
                        kategorijos[klausymas_del_trinimo].clear()
                        print()
                        print(f'Jusu sarasas "{klausymas_del_trinimo}" yra tuscias.')
                        print()
                        redagavimas()
                    elif temos_kiekio_trinimas2 == "n":
                        trinimas_pasirinktu()
                    else:
                        print(style.RED + "Klaidingai ivedete atsakyma! Bandykite dar karta!")
                        print(style.RESET)
                        trinimas_pasirinktu()
            except ValueError:
                print(style.RED + "Klaidingai ivedete atsakyma! Bandykite dar karta!")
                print(style.RESET)
                trinimas_pasirinktu()


        def def_trinimo_repeatas():
            for y, z in enumerate(sarasas_meniu4):
                print(f'{y + 1} - {z}')
            print()
            try:
                klausymas_del_trinimo2 = int(input(style.BLUE + "Pasirinkite veiksma: " + style.RESET))
                if klausymas_del_trinimo2 == 1:
                    kategorijos[klausymas_del_trinimo].clear()
                    print()
                    print(f'Jusu sarasas "{klausymas_del_trinimo}" yra tuscias.')
                    print()
                    redagavimas()
                elif klausymas_del_trinimo2 == 2:
                    trinimas_pasirinktu()
                else:
                    print(style.RED + "Klaidingai pasirinkote veiksma! Bandykite dar karta.")
                    print(style.RESET)
                    def_trinimo_repeatas()
            except ValueError:
                print(style.RED + "Klaidingai pasirinkote veiksma! Bandykite dar karta.")
                print(style.RESET)
                def_trinimo_repeatas()


        for y, z in enumerate(sarasas_meniu4):
            print(f'{y + 1} - {z}')
        print()
        try:
            klausymas_del_trinimo2 = int(input(style.BLUE + "Pasirinkite veiksma: " + style.RESET))
            if klausymas_del_trinimo2 == 1:
                kategorijos[klausymas_del_trinimo].clear()
                print()
                print(f'Jusu sarasas "{klausymas_del_trinimo}" yra tuscias.')
                print()
                redagavimas()
            elif klausymas_del_trinimo2 == 2:
                print()
                for i2, x2 in enumerate(kategorijos[klausymas_del_trinimo]):
                    print(f'{i2 + 1} - {x2}')
                print()


                try:
                    temos_kiekio_trinimas = int(input(style.BLUE + "Kiek uzduociu norite istrinti? " + style.RESET))
                    trinimai = 0
                    if temos_kiekio_trinimas < len(kategorijos[klausymas_del_trinimo]):
                        while trinimai < temos_kiekio_trinimas:
                            trinimai += 1
                            try:
                                temos_delete = int(input(style.BLUE + "Iveskite skaiciu, kokia uzduoti norite istrinti: " + style.RESET))
                                kategorijos[klausymas_del_trinimo].pop(temos_delete - 1)
                                print()
                                for i2, x2 in enumerate(kategorijos[klausymas_del_trinimo]):
                                    print(f'{i2 + 1} - {x2}')
                                print()
                            except ValueError:
                                print()
                                print(style.RED + "Klaidingai ivedete uzduoties numeri! Bandykite dar karta." + style.RESET)
                                def_trinimo_repeatas()
                        meniu_def()
                    elif temos_kiekio_trinimas >= len(kategorijos[klausymas_del_trinimo]):
                        temos_kiekio_trinimas2 = input(style.BLUE + "Ivedete daugiau arba tiek pat trinimu kiek yra uzduociu sarase. Gal norite istrinti viska? y/n\n" + style.RESET)
                        if temos_kiekio_trinimas2 == "y":
                            kategorijos[klausymas_del_trinimo].clear()
                            print()
                            print(f'Jusu sarasas "{klausymas_del_trinimo}" yra tuscias.')
                            print()
                            redagavimas()
                        elif temos_kiekio_trinimas2 == "n":
                            trinimas_pasirinktu()
                        else:
                            print(style.RED + "Klaidingai ivedete atsakyma! Bandykite dar karta!")
                            print(style.RESET)
                            trinimas_pasirinktu()
                except ValueError:
                    print()
                    print(style.RED + "Klaidingai ivedete uzduociu kieki! Bandykite dar karta." + style.RESET)
                    def_trinimo_repeatas
            else:
                print(style.RED + "Klaidingai pasirinkote veiksma! Bandykite dar karta.")
                print(style.RESET)
                def_trinimo_repeatas()
        except ValueError:
            print(style.RED + "Klaidingai pasirinkote veiksma! Bandykite dar karta.")
            print(style.RESET)
            def_trinimo_repeatas()
    else:
        print(style.RED + "Klaidingai ivedete kategorijos pavadinima! Bandykite dar karta.")
        print(style.RESET)
        trinimas_temos()


def trinimas_vieno():
    print()
    for i in kategorijos:
        print(i)
    print()
    trinti_kategorija = input(style.BLUE + "Irasykite kokia kategorija norite istrinti: " + style.RESET)
    if trinti_kategorija in kategorijos:
        kategorijos.pop(trinti_kategorija)
        print()
        for i in kategorijos:
            print(i)
        print()
        if len(kategorijos) > 0:
            trinti_kategorija2 = input(style.BLUE + "Ar norite istrinti dar kategoriju? y/n\n" + style.RESET)
            if trinti_kategorija2 == "y":
                trinimas_vieno()
            elif trinti_kategorija2 == "n":
                redagavimas()
            else:
                print(style.RED + 'Klaidingai nurodete atsakyma "y/n"! Bandykite dar karta.' + style.RESET)
                trinimas_vieno()
        elif len(kategorijos) == 0:
            meniu_def()
    else:
        print(style.RED + "Netaisiklingai nurodyta kategorija! Bandykite dar karta.")
        print(style.RESET)
        trinimas_vieno()


def redagavimas():
    if len(kategorijos) > 0:
        print()
        for i, x in enumerate(sarasas_meniu3):
            print(f"{i + 1} - {x}")
        print()
        try:
            meniu3 = int(input(style.BLUE + "Pasrinkite punkta is meniu: " + style.RESET))
            if meniu3 == 1:
                kategorijos.clear()
                print("Jusu sarasas yra tuscias.")
                print()
                meniu_def()
            elif meniu3 == 2:
                trinimas_vieno()
            elif meniu3 == 3:
                trinimas_temos()
            elif meniu3 == 4:
                meniu_def()
            else:
                print(style.RED + "\nBlogai nurodytas skaicius is meniu saraso! Bandykite dar karta.")
                print(style.RESET)
                redagavimas()
        except ValueError:
            print(style.RED + "\nBlogai nurodytas skaicius is meniu saraso! Bandykite dar karta.")
            print(style.RESET)
            redagavimas()
    elif len(kategorijos) < 1:
        print()
        print(style.RED + "Jusu sarasas tuscias! Bandykite sukurti nauja kategorija.")
        print(style.RESET)
        meniu_def()


def sub_kategorija():
    if len(kategorijos) > 0:
        print()
        for i in range(len(kategorijos)):
            print(f"{i + 1} - {list(kategorijos)[i]}")
        print()
        try:
            klausymas_del_kategorijos = int(input(style.BLUE + "I kokia kategorija norite prideti uzduoti? Pazymekite skaiciu: " + style.RESET))
            print()
            if klausymas_del_kategorijos <= len(kategorijos):
                try:
                    uzduociu_kiekis = int(input(style.BLUE + "Kiek norite prideti uzduociu? " + style.RESET))
                    uzduotys = 0
                    while uzduociu_kiekis != uzduotys:
                        kategorija = input(style.BLUE + "Kokia uzduoti prideti? " + style.RESET)
                        uzduotys += 1
                        tema = list(kategorijos)[klausymas_del_kategorijos - 1]
                        kategorijos[tema].append(kategorija)
                        print()
                        for i in kategorijos:
                            print()
                            print(i.upper())
                            print()
                            if len(kategorijos[i]) == 0:
                                print("Sarasas tuscias")
                            for x in kategorijos[i]:
                                print(f' - {x} - ')
                        print()
                except ValueError:
                    print()
                    print(style.RED + "Klaidingai ivedete uzduociu kieki! Bandykite dar karta.")
                    print(style.RESET)
                    sub_kategorija()


                def sub_sub_kategorija():
                    pratesimas = input(style.BLUE + "Ar norite testi kurti uzduotys? y/n " + style.RESET)
                    if pratesimas == "y":
                        sub_kategorija()
                    elif pratesimas == "n":
                        meniu_def()
                    else:
                        print(style.RED + 'Klaidingai nurodete "y/n"! Bandykite dar karta.')
                        print(style.RESET)
                        sub_sub_kategorija()


                pratesimas = input(style.BLUE + "Ar norite testi kurti uzduotys? y/n " + style.RESET)
                if pratesimas == "y":
                    sub_kategorija()
                elif pratesimas == "n":
                    meniu_def()
                else:
                    print(style.RED + 'Klaidingai nurodete "y/n"! Bandykite dar karta.')
                    print(style.RESET)
                    sub_sub_kategorija()
            elif klausymas_del_kategorijos > len(kategorijos):
                print(style.RED + "Neimanoma prideti i negzistuojancia kategorija uzduoties!. Bandykite dar karta.")
                print(style.RESET)
                sub_kategorija()
        except ValueError:
            print()
            print(style.RED + "Klaidingai ivedete skaiciu i kokia kategorija norite prideti uzduociu! Bandykite dar karta.")
            print(style.RESET)
            sub_kategorija()
    elif len(kategorijos) < 1:
        print()
        print(style.RED + "Jusu sarasas tuscias! Bandykite iskarto sukurti kategorija.")
        print(style.RESET)
        meniu_def()


def kategorijos_kurimas():
    new_kategorija = input(style.BLUE + "Iveskite kategorijos pavadinima: " + style.RESET)
    kategorijos[new_kategorija] = []
    for i in kategorijos:
        print()
        print(i.upper())
        print()
        if len(kategorijos[i]) == 0:
                print("Sarasas tuscias")
        for x in kategorijos[i]:
            print(f' - {x} - ')
    testi_klausymas = input(style.BLUE + "Ar norite testi kurti kategorijas? y/n\n" + style.RESET)
    if testi_klausymas == "y":
        kategorijos_kurimas()
    elif testi_klausymas == "n":
        meniu_def()
    else:
        print(style.RED + 'Klaidingai nurodete "y/n! Bandykite dar karta.')
        print(style.RESET)
        kategorijos_kurimas2()


def kategorijos_kurimas2():
    testi_klausymas = input(style.BLUE + "Ar norite testi kurti kategorijas? y/n\n" + style.RESET)
    if testi_klausymas == "y":
        kategorijos_kurimas()
    elif testi_klausymas == "n":
        meniu_def()
    else:
        print(style.RED + 'Klaidingai nurodete "y/n! Bandykite dar karta.')
        print(style.RESET)
        kategorijos_kurimas2()


def temos_perziura():
    print()
    for i in kategorijos:
        print(i)
    print()
    temos_klausymas = input(style.BLUE + "Kokia kategorija norite perziureti? " + style.RESET)
    if temos_klausymas in kategorijos:
        print()
        print(kategorijos[temos_klausymas])
        print()
        try:
            temos_klausymas2 = int(input(style.BLUE + "Norite prideti nauja uzduoti (paspauskite 1) ar norite istrinti paskutine uzduoti (paspauskite 2)? " + style.RESET))
            if temos_klausymas2 == 1:
                temos_klausymas_pridejimas = input(style.BLUE + "Kokia uzduoti norite prideti? " + style.RESET)
                kategorijos[temos_klausymas].append(temos_klausymas_pridejimas)
                print()
                print(kategorijos[temos_klausymas])
                print()


                def temos_klausymas_def():
                    temos_klausymas_pridejimas = input(style.BLUE + "Kokia uzduoti norite prideti? " + style.RESET)
                    kategorijos[temos_klausymas].append(temos_klausymas_pridejimas)
                    print()
                    print(kategorijos[temos_klausymas])
                    print()
                    temos_repeatas()


                def temos_repeatas():
                    temos_klausymas3 = input(style.BLUE + "Ar norite testi? y/n\n" + style.RESET)
                    if temos_klausymas3 == "y":
                        temos_klausymas_def()
                    elif temos_klausymas3 == "n":
                        meniu_def()
                    else:
                        print(style.RED + "Klaidingai ivedete atsakyma! Bandykite dar karta.")
                        print(style.RESET)
                        temos_repeatas()


                temos_klausymas3 = input(style.BLUE + "Ar norite testi? y/n\n" + style.RESET)
                if temos_klausymas3 == "y":
                    temos_klausymas_def()
                elif temos_klausymas3 == "n":
                    meniu_def()
                else:
                    print(style.RED + "Klaidingai ivedete atsakyma! Bandykite dar karta.")
                    print(style.RESET)
                    temos_repeatas()
            elif temos_klausymas2 == 2:
                kategorijos[temos_klausymas].pop(-1)
                temos_perziura()
        except ValueError:
            print(style.RED + "Klaidingai ivedete skaiciu! Bandykite dar karta.")
            print(style.RESET)
            temos_perziura()
    else:
        print(style.RED + "Klaidingai ivedete kategorijos pavadinima! Bandykite dar karta.")
        print(style.RESET)
        temos_perziura()


def meniu_def2():
    print()
    for i, x in enumerate(sarasas_meniu2):
        print(f"{i + 1} - {x}")
    print()
    try:
        meniu2 = int(input(style.BLUE + "Pasirinkite punkta is meniu: " + style.RESET))
        if meniu2 == 1:
            temos_perziura()
        elif meniu2 == 2:
            kategorijos_kurimas()
        elif meniu2 == 3:
            sub_kategorija()
        elif meniu2 == 4:
            redagavimas()
        elif meniu2 == 5:
            if len(kategorijos) > 0:
                formato_klausymas = input(style.BLUE + "Kokiu formatu norite issaugoti sarasa? txt ar csv? " + style.RESET)
                if formato_klausymas == "csv":
                    pavadinimas = input(style.BLUE + "Iveskite failo pavadinima: " + style.RESET)
                    save = csv.writer(open(f"{pavadinimas}.csv", "w"))
                    for k, v in kategorijos.items():
                        save.writerow([k, v])
                elif formato_klausymas == "txt":
                    pavadinimas2 = input(style.BLUE + "Iveskite failo pavadinima: " + style.RESET)
                    save2 = open(f"{pavadinimas2}.txt","w")
                    save2.write(str(kategorijos))
                    save2.close()
            elif len(kategorijos) == 0:
                print(style.RED + "Negalite issaugoti tuscio saraso! Pabandykite susikurti kategorija." + style.RESET)
                meniu_def()
            else:
                print(style.RED + "Blogai pasirinkote formata! Bandykite dar karta." + style.RESET)
                meniu_def()
        else:
            print(style.RED + "Blogai nurodytas skaicius is meniu saraso! Bandykite dar karta.")
            print(style.RESET)
            meniu_def()
    except ValueError:
        print(style.RED + "Blogai nurodytas skaicius is meniu saraso! Bandykite dar karta.")
        print(style.RESET)
        meniu_def()


def meniu_def():
    print()
    for i, x in enumerate(sarasas_meniu):
        print(f"{i + 1} - {x}")
    print()
    try:
        meniu = int(input(style.BLUE + "Pasirinkite punkta is meniu: " + style.RESET))
        if meniu == 1:
            if len(kategorijos) >= 1:
                for i in kategorijos:
                    print()
                    print(i.upper())
                    print()
                    if len(kategorijos[i]) == 0:
                        print("Sarasas tuscias")
                    for x in kategorijos[i]:
                        print(f' - {x} - ')
                meniu_def2()
            elif len(kategorijos) == 0:
                print(style.RED + "\nJusu sarasas yra tuscias.")
                print(style.RESET)
                meniu_def()
        elif meniu == 2:
            kategorijos_kurimas()
        elif meniu == 3:
            sub_kategorija()
        elif meniu == 4:
            redagavimas()
        elif meniu == 5:
            if len(kategorijos) > 0:
                formato_klausymas = input(style.BLUE + "Kokiu formatu norite issaugoti sarasa? txt ar csv? " + style.RESET)
                if formato_klausymas == "csv":
                    pavadinimas = input(style.BLUE + "Iveskite failo pavadinima: " + style.RESET)
                    save = csv.writer(open(f"{pavadinimas}.csv", "w"))
                    for k, v in kategorijos.items():
                        save.writerow([k, v])
            elif formato_klausymas == "txt":
                pavadinimas2 = input(style.BLUE + "Iveskite failo pavadinima: " + style.RESET)
                save2 = open(f"{pavadinimas2}.txt","w")
                save2.write(str(kategorijos))
                save2.close()
            elif len(kategorijos) == 0:
                print(style.RED + "Negalite issaugoti tuscio saraso! Pabandykite susikurti kategorija." + style.RESET)
                meniu_def()
            else:
                print(style.RED + "Blogai pasirinkote formata! Bandykite dar karta." + style.RESET)
                meniu_def()
        else:
            print(style.RED + "\nBlogai nurodytas skaicius is meniu saraso! Bandykite dar karta.")
            print(style.RESET)
            meniu_def()
    except ValueError:
        print(style.RED + "\nBlogai nurodytas skaicius is meniu saraso! Bandykite dar karta.")
        print(style.RESET)
        meniu_def()


try:
    meniu = int(input(style.BLUE + "Pasirinkite punkta is meniu: " + style.RESET))
    if meniu == 1:
        if len(kategorijos) >= 1:
            for i in kategorijos:
                print()
                print(i.upper())
                print()
                if len(kategorijos[i]) == 0:
                    print("Sarasas tuscias")
                for x in kategorijos[i]:
                    print(f' - {x} - ')
            meniu_def2()
        elif len(kategorijos) == 0:
            print(style.RED + "\nJusu sarasas yra tuscias.")
            print(style.RESET)
            meniu_def()
    elif meniu == 2:
        kategorijos_kurimas()
    elif meniu == 3:
        sub_kategorija()
    elif meniu == 4:
        redagavimas()
    elif meniu == 5:
        if len(kategorijos) > 0:
            formato_klausymas = input(style.BLUE + "Kokiu formatu norite issaugoti sarasa? txt ar csv? " + style.RESET)
            if formato_klausymas == "csv":
                pavadinimas = input(style.BLUE + "Iveskite failo pavadinima: " + style.RESET)
                save = csv.writer(open(f"{pavadinimas}.csv", "w"))
                for k, v in kategorijos.items():
                    save.writerow([k, v])
            elif formato_klausymas == "txt":
                pavadinimas2 = input(style.BLUE + "Iveskite failo pavadinima: " + style.RESET)
                save2 = open(f"{pavadinimas2}.txt","w")
                save2.write(str(kategorijos))
                save2.close()
            else:
                print(style.RED + "Blogai pasirinkote formata! Bandykite dar karta." + style.RESET)
                meniu_def()
        elif len(kategorijos) == 0:
            print(style.RED + "Negalite issaugoti tuscio saraso! Pabandykite susikurti kategorija." + style.RESET)
            meniu_def()
    else:
        print(style.RED + "\nBlogai nurodytas skaicius is meniu saraso! Bandykite dar karta.")
        print(style.RESET)
        meniu_def()
except ValueError:
    print(style.RED + "\nBlogai nurodytas skaicius is meniu saraso! Bandykite dar karta.")
    print(style.RESET)
    meniu_def()
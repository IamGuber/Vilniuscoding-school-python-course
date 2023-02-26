# Sukurkite skaičiaus atspėjimo užduotį. Leiskite vartotojui pasirinkti žaidimo sudėtingumą 
# (atsitiktinio skaičiaus rėžiai), ar suteikiamos pagalbos (skaičius mažesnis/didesnis nei spėjamas), 
# kiek spėjimų leidžiama (neribotai, arba pvz iki 10 ėjimų), bei kiti pasirinkti parametrai. 
# Vartotojas šiuos parametrus pasirenka žaidimo pradžioje. Turite užtikrinti, 
# kad vartotojas pasirinko parametrus tik iš galimų - jeigu ne, liepkite įvedimą pakartoti.

import random


vartotojo_skc = int(input("Iveskite skaiciu iki kiek norite speti skaicius: "))
pagalba = input("Ar reikalinga pagalba speliojant? Y/N: ")
ribojimas = int(input("Jeigu norite apriboti spejimu skaiciu iveskite. Jeigu ne iveskite 0.: "))
slaptas_skc = random.randint(1, vartotojo_skc)
spejimu_skc = 0

spejimas = None

while slaptas_skc != spejimas:
    print("Spekite skaiciu nuo 1 iki", vartotojo_skc, ": ")
    spejimas = int(input("Iveskite skaiciu: "))

    if pagalba == "Y":

        if ribojimas == 0:
            if spejimas < slaptas_skc:
                print("Bandykite didesni skaiciu.")
            elif spejimas > slaptas_skc:
                print("Bandykite mazesni skaiciu.")
            else:
                print("Atspejote!")

        elif ribojimas != 0:
            spejimu_skc += 1
            if spejimu_skc == ribojimas:
                print("Praleimejote!")
                break
            if spejimas < slaptas_skc:
                print("Bandykite didesni skaiciu.")
            elif spejimas > slaptas_skc:
                print("Bandykite mazesni skaiciu.")
            else:
                print("Atspejote!")

    elif pagalba == "N":

        if ribojimas == 0:
            if spejimas < slaptas_skc:
                print("Bandykite dar karta.")
            elif spejimas > slaptas_skc:
                print("Bandykite dar karta.")
            else:
                print("Atspejote!")
        
        elif ribojimas != 0:
            spejimu_skc += 1
            if spejimu_skc == ribojimas:
                print("Praleimejote!")
                break
            if spejimas < slaptas_skc:
                print("Bandykite dar karta.")
            elif spejimas > slaptas_skc:
                print("Bandykite dar karta.")
            else:
                print("Atspejote!")
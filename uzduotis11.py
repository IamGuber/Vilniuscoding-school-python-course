# Leiskite vartotojui nurodyti rėžių pradžią, pabaigą, žingsnį. 
# Taip pat, kokius skaičius jis nori matyti (lyginius ar nelyginius). 
# Patikrinkite ar rėžiai tinkami, jei taip vykdykite ciklą, kuris eitų per nurodytą rėžių, darant atitinkamą žingsnį. 
# Išveskite tik tokius skaičius kokius vartotojas pasirinko (lyginius arba nelyginius).

pradzia = int(input("Iveskite pradzia: "))
pabaiga = int(input("Iveskite pabaiga: "))
zingsnis = int(input("Iveski zingsni: "))

pirmas_klausymas = input("Kokius skaicius norite matyti? Lyginius ar nelyginius?: ")

if pradzia < pabaiga:
    if pirmas_klausymas.lower() == "lyginius":
        for ckl in range(pradzia, pabaiga, zingsnis):
            if ckl % 2 == 0:
                print(ckl)
if pirmas_klausymas.lower() == "nelyginius":
    for ckl in range(pradzia, pabaiga, zingsnis):
        if ckl % 2 != 0:
            print(ckl)
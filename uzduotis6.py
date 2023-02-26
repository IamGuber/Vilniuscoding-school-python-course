# Vartotojas turi suvesti rėžių pradžią ir pabaigą. 
# Tačiau jūs turite patikrinti ar nurodyti rėžiai yra geri (pradžia mažesnė už pabaigą). 
# Liepkite vartotojui kartoti įvedimą tol, kol rėžiai jau bus įvesti tinkamai. 
# Turint tinkamus rėžius, išveskite visus skaičius nuo rėžių pradžios iki pabaigos 
# (šitam jau vietoj while galite naudoti for ciklą), šalia kiekvieno skaičiaus išvedant jo kvadratą, bei ar jis lyginis/nelyginis.

while True:
    pradzia = int(input("Iveskite pradzia: "))
    pabaiga = int(input("Iveskite pabaiga: "))
    if pradzia > pabaiga or pradzia == pabaiga:
        print("Blogi reziai! Kartokite is naujo.")
    else:
        break
for x in range(pradzia, pabaiga):
    if x % 2 == 0:
        print(x, "- lyginis", "Skaiciaus kvadratas: ", x ** 2)
    if x % 2 != 0:
        print(x, "- nelyginis", "Skaiciaus kvadratas: ", x ** 2)
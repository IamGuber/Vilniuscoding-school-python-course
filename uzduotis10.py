# Vartotojui išveskite pasirinkto skaičiaus daugybos lentelę 
# (pvz, skaičiaus 5 daugybos lentelė būtų 5 * 1 = 5; 5 * 2 = 10; 5 * 3 = 15; ...). 
# Leiskite vartotojui kartoti veiksmą (tiek kartų kiek norės) ir gauti dar vieną daugybos lentelę su kitu pasirinktu skaičiumi.

kartojimas = "Y"
daugybos_lentele = range(1, 10)

while kartojimas == "Y":
    skc = int(input("Iveskite skaiciu is kurio norite gauti daugybos lentele: "))
    for x in daugybos_lentele:
        print(f"{skc} * {x} = {skc * x}")
    kartojimas = input("Ar norite testi? Y/N ")
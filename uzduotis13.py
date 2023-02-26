# Leiskite vartotojui įvesti bet kokį žodį, bei pasirinkti po kiek kartų turėtų būti pakartojama kiekviena raidė. 
# Su ciklo pagalba išveskite kiekvieną raidę iš žodžio atskiroje eilutėje, 
# taip pat, tą raidę eilutėje kartokite tiek kartų kiek pasirinko vartotojas (16 pvz).

zodis = input("Iveskite zodi: ")
kartojimas = int(input("Iveskite skaiciu kiek kartu turetu kartotis viena raide: "))

for x in zodis:
    print(x * kartojimas)
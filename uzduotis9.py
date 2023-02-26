# Leiskite vartotojui atlikti norimus skaičiavimus tiek kartų kiek jis nori. 
# Pavyzdžiui, leiskite vartotojui įvesti du skaičius, tuomet jam parodykite pačius skaičius, veiksmus 
# (sudėtis, atimtis, daugyba, dalyba) ir suskaičiuotus atsakymus (5 + 3 = 8; 5 - 3 = 2; ...). 
# Kai atsakymai bus parodyti, vartotojas turi turėti galimybę pakartoti skaičiavimus, 
# todėl leiskite pasirinkti ar dar kartoti veiksmą, ar jau programa turėtų baigti savo darbą.

kartojimas = "Y"

while kartojimas == "Y":
    pirmas = int(input("Iveskite pirma skaiciu: "))
    antras = int(input("Iveskite antra skaiciu: "))
    print(f"{pirmas} + {antras} = {pirmas + antras}")
    print(f"{pirmas} - {antras} = {pirmas - antras}")
    print(f"{pirmas} * {antras} = {pirmas * antras}")
    print(f"{pirmas} / {antras} = {pirmas / antras}")
    kartojimas = input("Ar norite testi skaiciavimus? Y/N ")
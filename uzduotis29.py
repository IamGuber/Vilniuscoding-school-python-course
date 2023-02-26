# Sukurkite programą, kurioje vartotojas galėtų įvesti norimą kiekį žodžių 
# (pasirenka iš pradžių ir vykdomas for iki to kiekio skaičiaus, arba vykdomas while kol neįveda q ar kokio kito simbolio/žodžio). 
# Išveskite visus šiuos žodžius ekrane.

print("Iveskite kiek zodziu noresite ivesti?")
kiekis = int(input())
sarasas = []

for i in range(kiekis):
    print("Iveskite", i + 1, "-a, zodi:")
    x = str(input())
    sarasas.append(x)

print(sarasas)
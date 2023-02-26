# Liepkite vartotojui įvesti kiek jis nori skaičių. 
# Įvedimą sustabdykite tuomet, kai vartototojas įves 0 ar -1, ar kitą jūsų pasirinktą skaičių ar simbolį. 
# Raskite vartotojo įvestų skaičių sumą, vidurkį.

skc = -1
suma = 0
skc_kiekis = 0

while skc != 0:
    skc = int(input("Iveskite skaiciu: "))
    print("Norint uzbaigti ivedima, iveskite '0'")
    if skc != 0:
        skc_kiekis += 1
        suma += skc

print()

vidurkis = suma / skc_kiekis
print("Skaiciu suma:", suma, "Vidurkis:", vidurkis)
print()
print("Pabaiga.")
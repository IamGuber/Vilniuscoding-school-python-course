# Liepkite vartotojui įvedinėti bet kokius skaičius. Vykdykite įvedinėjimą iki kol įvestas skaičius bus lygus 0. 
# Raskite įvestų skaičių sumą.

skc = -1
sarasas = []

while skc != 0:
    skc = int(input("Iveskite skaiciu: "))
    sarasas.append(skc)
for x in sarasas:
    suma = x + x
print(suma)
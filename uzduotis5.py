# Sukurkite pasirinktą list ir užpildykite jį duomenimis. 
# Iš jo pašalinkite keletą įrašų, tiesiog parašant pop() funkciją. 
# Taip pat, sukurkite, kad vartotojas galėtų pasirinkti kiek dar duomenų pašalinti ir pašalinkite iš list pasirinktą kiekį įrašų.

sarasas = [40, 3, 56, 7, 88, 90, 43]
print(sarasas)

sarasas.pop(0)

print(sarasas)

print("Kiek dar noretume pasalinti duomenu?")
salinimas = int(input())

suma = 0

while suma != salinimas:
    pasirinkimas = int(input("Pasirinkite kuri duomeni pasalinti?: "))
    indeksas = sarasas.index(pasirinkimas)
    sarasas.pop(indeksas)
    suma += 1

print(sarasas)
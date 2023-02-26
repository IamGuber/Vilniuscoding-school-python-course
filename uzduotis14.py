# Pamėginkite sukurti žodžių žodyną. Šį žodyną turėtų užpildyti vartotojas, įvesdamas visus norimus žodžius. 
# Po kiekvieno įvedimo jam turėtų būti parodomi visi žodžiai, tačiau surikiuoti, t.y. įdėjus žodį į sąrašą, jį surikiuokite iš naujo.

sarasas = []

papildymas = input("Iveskite per kableli kokiais zodziais noretumete papildyti zodyna: ")
isarasa = papildymas.split(",")
sarasas.extend(isarasa)

print(sarasas)
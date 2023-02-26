# Susikurkite tuple iš studijų programos modulių pavadinimų. 
# Atspausdinkite šiuos pavadinimus sąraše, prieš kiekvieną pavadinimą išvedant brūkšniuką. 
# Raskite ilgiausią modulio pavadinimą.

info = ("Matematika", "Fizika", "Chemija", "Literaturos")

for i in info:
    print("-", i)

ilgiausias_zodis = info[0]
for i in info:
    if len(i) > len(ilgiausias_zodis):
        ilgiausias_zodis = i
print("Ilgiausias zodis yra", ilgiausias_zodis)
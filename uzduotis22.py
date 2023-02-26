# Susikurkite sąrašą prekių krepšeliui saugoti. Išveskite kiek prekių krepšelyje yra narių. 
# Tuomet išveskite visą prekių krepšelio informaciją, nurodant kelinta prekė, pvz "nr 1 pirkinys:", "nr 2 pirkinys:" ir t.t.

sarasas = ["Duona", "Arbuzas", "Sviestas", "Pienas", "Varske", "Desra"]

print("Prekiu krepselyje:", len(sarasas))

for indeks, preke in enumerate(sarasas, start = 1):
    print(indeks, preke)
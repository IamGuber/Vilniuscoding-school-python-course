# Susikurkite skaičių masyvą ir užpildykite jį duomenimis. 
# Išveskite visus skaičius atskirose eilutėse. Prie kiekvieno lyginio skaičiaus dar išvedant jo kvadratą.

sarasas = list(range(1, 20))

for i in sarasas:
    print(i, "skaiciaus kavadratas yra:", i ** 2)
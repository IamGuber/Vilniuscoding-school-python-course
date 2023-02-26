# Susikurkite skaičių sąrašą ir užpildykite duomenimis. 
# Raskite visų skaičių, kurie dalinasi iš 3 sumą ir vidurkį. Išveskite pradinius duomenis ir gautus atsakymus.

sarasas = list(range(1, 20))
redaguotas = []
print("Pradinis sarasas:", sarasas)

for i in sarasas: 
    if i % 3 == 0:
        redaguotas.append(i)

print("Redaguotas sarasas:", redaguotas)
print("Suma redaguoto:", sum(redaguotas))
print("Vidurkis redaguoto:", round(sum(redaguotas) / len(redaguotas), 2))
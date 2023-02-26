# Susikurkite sąrašą norimiems žodžiams saugoti. Užpildykite šį sąrašą duomenimis. 
# Į kitą sąrašą atrinkite tuos žodžius, kurie yra trumpi (sudaro mažiau nei 5 raidės). 
# Išveskite pradinius duomenis ir atrinktus.

sarasas = ["vienas", "du", "trys", "keturi", "penki", "sesi", "septyni"]
trumpi_zodziai = []

for i in sarasas:
    if len(i) < 5:
        trumpi_zodziai.append(i)

print(sarasas)
print(trumpi_zodziai)

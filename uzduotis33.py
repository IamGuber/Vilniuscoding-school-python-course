# Sugeneruokite 100-ą atsitiktinių skaičių ir sukelkite visus tuos skaičius į sąrašą. Atlikite šiuos veiksmus:
# Raskite mažiausią skaičių, didžiausią skaičių, bei vidurkį.
# Tuomet atrinkite į atskirą sąrašą skaičius, kurie žemesni nei vidurkis. Raskite šių skaičių vidurkį.
# Taip pat, atrinkite į dar vieną sąrašą skaičius, kurie didesni nei vidurkis. Raskite šių skaičių vidurkį.
# Ekrane išveskite pradinius duomenis, mažiausią ir didžiausią skaičius, rastą vidurkį, pirmus atrinktus skaičius ir jų vidurkį, 
# antrus atrinktus skaičius ir jų vidurkį.

import random

sarasas = []

for i in range(100):
    sarasas.append(random.randint(1, 100))

vidurkis = round(sum(sarasas) / len(sarasas), 2)

sarasas.sort()
print(sarasas[0])
sarasas.reverse()
print(sarasas[0])
print(vidurkis)

print()

m_sarasas = []

for x in sarasas:
    if x < vidurkis:
        m_sarasas.append(x)

m_vidurkis = round(sum(m_sarasas) / len(m_sarasas), 2)
print(m_sarasas)
print(m_vidurkis)

print()

d_sarasas = []

for y in sarasas:
    if y > vidurkis:
        d_sarasas.append(y)

d_vidurkis = round(sum(d_sarasas) / len(d_sarasas), 2)
print(d_sarasas)
print(d_vidurkis)
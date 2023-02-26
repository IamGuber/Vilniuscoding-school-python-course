# Susikurkite sąrašą, kuriame būtų saugomos jau praeitos Python temos. Išveskite tekstą "mes jau mokėmės:". 
# Ir iškart po to atskirose eilutėse visas temas, tačiau jas sunumeruokite "1-a tema:", "2-a tema:" ir t.t. 
# Tai pamėginkite atlikti tiek su for ciklu, tiek su while ciklu.

sarasas = ["Skaiciai ir matematika", "Kintamieji", "Informacijos isvedimas", "Skaiciai ir matematika2", "Informacijos isvedimas2",
"Patikrinimo salyga 'if'"]

print("Mes jau mokemes:")

for temos in range(len(sarasas)):
    print(f"{temos +1}-a tema {sarasas[temos]}")

print()

temos2 = 0

while temos2 < len(sarasas):
    print(f"{temos2 +1}-a tema {sarasas[temos2]}")
    temos2 += 1
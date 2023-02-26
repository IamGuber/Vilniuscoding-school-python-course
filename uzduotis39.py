# Susikurkite žodžių sąrašą ir užpildykite duomenimis. 
# Išveskite visus žodžius ekrane, nurodant iš kiek raidžių kiekvienas šis žodis yra sudarytas. 
# Papildykite programą taip, kad rastumėte visų raidžių kiekį (pvz yra žodžiai "medis" ir "alus", 5 ir 4 raidės atitinkamai, 
# o jas sudėjus gaunasi 9 raidės).

sarasas = ["vienas", "du", "trys", "keturi", "penki", "sesi", "septini"]

visos_raides = 0

for i in sarasas:
    print(i, "raidziu zodyje:", len(i))
    visos_raides += len(i)

print("Suma visu raidziu:", visos_raides)
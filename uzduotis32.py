# Susikurkite žodžių sąrašą. Raskite ir išveskite trumpiausią ir ilgiausią žodžius, bei jų raidžių kiekius.

sarasas = ["vienas", "du", "trys", "keturi", "penki", "sesi", "septini"]

sarasas.sort(key=len)
trumpiausias = sarasas[0]
print(trumpiausias, "raidziu zodyje yra:", len(trumpiausias))

sarasas.reverse()
ilgiausias = sarasas[0]
print(ilgiausias, "raidziu zodyje yra:", len(ilgiausias))
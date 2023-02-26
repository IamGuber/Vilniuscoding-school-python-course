# Išveskite visus skaičius nuo 1 iki 100 arba iki tol kol pasitaikys toks, kuris dalinasi iš 7.

sk = 0

while sk < 101:
    sk += 1
    if sk % 7 == 0:
        break
    print(sk)
# Išvedinėkite visus skaičius nuo 1 iki tol kol pasitaikys skaičius, kuris dalinasi iš 3 ir iš 5.

sk = 1

while sk > 0:
    print(sk)
    if sk % 3 == 0 and sk % 5 == 0:
        break
    sk += 1
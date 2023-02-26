# Išveskite visus skaičius nuo 1 iki 15, prie kiekvieno jų nurodant tai lyginis ar nelyginis skaičius. Pvz:
# 1 - nelyginis
# 2 - lyginis
# 3 - nelyginis
# itt.

for sk in range(1, 15):
    if sk % 2 == 0:
        print(sk, "- lyginis")
    if sk % 2 != 0:
        print(sk, "- nelyginis")
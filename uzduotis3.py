# Išveskite visus skaičius nuo 25 iki 50. Vietoj skaičių, kurie dalinasi iš 3 išveskite tekstą "dalinasi iš 3".

sk = range(25, 51)

for x in sk:
    if x % 3 == 0:
        print("dalinasi is 3")
        continue
    print(x)
# Išveskite visus skaičius nuo 1 iki 50. 
# Prie kiekvieno lyginio skaičiaus parašykite žodį "lyginis", o prie kiekvieno nelyginio – "nelyginis".

sk = 1

while sk < 51:
    if sk % 2 == 0:
        print(sk, "lyginis")
    if sk % 2 != 0:
        print(sk, "nelyginis")
    sk += 1
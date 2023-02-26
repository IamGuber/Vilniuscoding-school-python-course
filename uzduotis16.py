# Raskite visų lyginių skaičių nuo 20 iki 50 sumą.

suma = 0

for x in range(20, 51):
    if x % 2 == 0:
        suma = suma + x
print(suma)
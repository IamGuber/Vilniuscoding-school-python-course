# Raskite visų nelyginių skaičių nuo 30 iki 60 sumą.

suma = 0

for x in range(30, 61):
    if x % 2 != 0:
        suma = suma + x
print(suma)
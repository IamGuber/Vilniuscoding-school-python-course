# Rasti visų skaičių, žemesnių už 1000 ir kurie dalinasi iš 3 arba 5, sumą. Pavyzdys:
#	Visi skaičiai mažesni už 10 ir kurie dalinasi iš 3 arba 5 yra: 3, 5, 6, 9.
#	Šių skaičių suma yra 23.
# Turite gauti 233168 atsakymą.

suma = 0 
for x in range(0, 1000):
    if x % 3 == 0 or x % 5 == 0:
        suma = suma + x
print(suma)
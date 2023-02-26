# Susikurkite sąrašą ir jį užpildykite skaičiais (savarankiškai arba atsitiktiniais). 
# Iš pradžių išveskite tekstą "lyginiai skaičiai" ir visus lyginius skaičius. 
# Tuomet išveskite tekstą "visi nelyginiai skaičiai" ir visus nelyginius skaičius. 
# Bei ant galo tekstą "visi skaičiai, kurie dalinasi iš 3" ir visus skaičius, kurie atitinka tokią sąlygą.

sarasas = [1, 11, 2, 22, 3, 33, 4, 44, 5, 55]

print("Lyginiai skaiciai:")
for lyg in sarasas:
    if lyg % 2 == 0:
        print(lyg)

print("Nelyginiai skaiciai:")
for nelyg in sarasas:
    if nelyg % 2 != 0:
        print(nelyg)

print("Skaiciai kurie dalinasi is 3: ")
for other in sarasas:
    if other % 3 == 0:
        print(other)
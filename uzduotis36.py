# Susikurkite skaičių masyvą ir užpildykite jį atsitiktiniais skaičiais. Raskite visų skaičių, kurie dalinasi iš 4 sumą.

sarasas = list(range(5, 55))

for i in sarasas:
    if i % 4 == 0:
        print("Skaicius", i, "dalinasi is 4.")
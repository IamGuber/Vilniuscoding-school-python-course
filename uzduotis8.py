# Susikurkite kintamuosius rėžių pradžiai ir pabaigai nusakyti.
# Patikrinkite, kad tai būtų validu (pradžia turi būti mažesnė nei pabaiga).
# Jei rėžiai tinkami, tuomet vykdyti for, kuris iš duotų skaičių išvestų visus nelyginius skaičius arba tuos, kurie dalinasi iš 8.

pradzia, pabaiga = 1, 26
if pradzia < pabaiga:
    for sk in range(pradzia, pabaiga):
        if sk % 2 != 0 or sk % 8 == 0:
            print(sk)
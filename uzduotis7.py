# Susikurkite kintamuosius rėžių pradžiai ir pabaigai nusakyti. 
# Patikrinkite, kad tai būtų validu (pradžia turi būti mažesnė nei pabaiga). Jei rėžiai tinkami, tuomet vykdyti for, 
# kuris atskirose eilutėse išvestų kiekvieną skaičių iš tų rėžių, bei atskiriant tarpu - tų skaičių kvadratus.

pradzia, pabaiga = 0, 10

if pradzia < pabaiga:
    for sk in range(pradzia, pabaiga):
        print(sk, sk ** 2)
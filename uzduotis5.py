# Sukurkite funkciją, kurios viduje sugeneruotumėte du atsitiktinius skaičius. 
# Funkcijoje suskaičiuokite ir išveskite šių dviejų skaičių sumą, kartu išvedant ir patį atliekamą veiksmą (pvz 7 + 2 = 9). 
# Iškvieskite šią funkciją keletą kartų.

import random

def info():
    skaicius1 = random.randint(1, 100)
    skaicius2 = random.randint(1, 100)
    suma = skaicius1 + skaicius2
    print(f"{skaicius1} + {skaicius2} = {suma}")

info()
info()
info()
info()
info()
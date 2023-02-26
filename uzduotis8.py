# Sukurkite funkciją, kuri išvestų atsitiktinį skaičių. Už funkcijos ribų sukurkite ciklą, kurį būtų vykdomas 10 kartų. 
# Iškvieskite sukurtą funkciją cikle. Turėtumėte pamatyti 10 atsitiktinių skaičių.

import random

def info():
    skaicius = random.randint(1, 100)
    print(skaicius)

skc = 0
while skc != 10:
    info()
    skc += 1
# Susikurkite du skaičius. Patikrinkite (naudojant 4 atskirus if’us):
# ar pirmas skaičius yra didesnis už antrąjį arba yra lygus 0;
# ar antras skaičius yra didesnis už pirmąjį arba yra lygus 5;
# ar pirmas skaičius yra didesnis už antrąjį ir yra lygus 20;
# ar antras skaičius yra didesnis už pirmąjį ir yra mažesnis už 100;

skc1 = 10
skc2 = 6

if skc1 > skc2 or skc1 == 0:
    print("ar pirmas skaičius yra didesnis už antrąjį arba yra lygus 0")
if skc2 > skc1 or skc2 == 5:
    print("ar antras skaičius yra didesnis už pirmąjį arba yra lygus 5")
if skc1 > skc2 and skc1 == 20:
    print("ar pirmas skaičius yra didesnis už antrąjį ir yra lygus 20")
if skc2 > skc1 and skc2 < 100:
    print("ar antras skaičius yra didesnis už pirmąjį ir yra mažesnis už 100")
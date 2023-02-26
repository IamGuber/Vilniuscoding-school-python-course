# Sukurkite funkciją, kuriai perduotumėte du skaičius. Ši funkcija turi rasti kuris skaičius yra didesnis ir išvesti gautą atsakymą, 
# o jei skaičiai lygūs - tuomet išvesti, kad skaičiai lygūs. Iškvieskite šią funkciją keletą kartų, duodant skirtingus skaičius.

def info(skc1, skc2):
    if skc1 > skc2:
        print("Skaicius", skc1, "didesnis uz skaciu", skc2)
    elif skc1 < skc2:
        print("Skaicius", skc2, "didesnis uz skaciu", skc1)
    else:
        print("Skaiciai", skc1, "ir", skc2, "yra lygus.")

info(5, 10)
info(8, 4)
info(2, 2)
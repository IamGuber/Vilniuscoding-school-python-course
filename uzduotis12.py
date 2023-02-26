# Leiskite vartotojui suvesti tris skaičius. Suraskite kuris iš šių skaičių yra didžiausias.

skc1 = int(input("Iveskite pirma skaiciu: "))
skc2 = int(input("Iveskite antra skaiciu: "))
skc3 = int(input("Iveskite trecia skaiciu: "))

if(skc1 > skc2 > skc3):
    print("Primas skaicius didziausias.")
elif(skc1 < skc2 < skc3):
    print("Trecias skaicius didziausias.")
elif(skc2 > skc1 > skc3):
    print("Antras skaicius didziausias")
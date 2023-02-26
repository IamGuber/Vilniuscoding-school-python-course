# Liepkite vartotojui suvesti savo amžių. Patikrinkite ar amžius yra didesnis arba lygus 18-ai, jei taip - išveskite "jūs galite balsuoti".

amzius = int(input("Iveskite savo amziu: "))

if amzius >= 18:
    print("Jus galite balsuoti.")
if amzius < 18:
    print("Jums maziau nei 18m. balsuoti negalima!")
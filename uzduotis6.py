# Sukurkite list su pasirinktais duomenimis. 
# Patikrinkite ar sąraše yra daugiau nei 5 įrašai ir jeigu taip - jį išvalykite (clear funkcija).

sarasas = [3, 78, 90, 555, 2, 34]
print(sarasas)

klausymas = "N"
while klausymas == "N":
    klausymas = input("Istrinti viena duomeni? Y/N: ")
    if klausymas == "Y":
        sarasas.pop()
        print(sarasas)
    elif klausymas == "N":
        len(sarasas) > 5
        sarasas.clear()
        print(sarasas)
        break
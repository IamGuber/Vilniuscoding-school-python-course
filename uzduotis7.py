# Sukurkite list, kuriame būtų surašyti bet kokie žodžiai. 
# Leiskite vartotojui atlikti paiešką tame sąraše - vartotojas įvestų norimą žodį ir programa pasakytų ar 
# tame sąraše tas žodis yra ir jeigu yra, tai kurioje vietoje.

sarasas = ["Darius", "Vasaris", "Donatas", "Julija", "Ugne", "Egle"]

klausymas = input("Iveskite koki varda norite surasti sarase?: ")

paieska = klausymas in sarasas
if paieska == False:
    print("Tokio vardo sarase nera.")
elif paieska == True:
    vieta = sarasas.index(klausymas) + 1
    print("Vardas sarase yra. Jis randasi", vieta, "saraso vietoje.")
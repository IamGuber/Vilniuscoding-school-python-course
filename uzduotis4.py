# Sukurkite dvi funkcijas, kur vienoje būtų viena teksto eilutėje, kitoje kita. 
# Sukurkite trečią funkciją, kuri iškviestų pirmas dvi funkcijas. Iškvieskite šią trečiąją funkciją už visų funkcijų ribų.

def pirma_fun():
    print("Pirmas tekstas.\n")

def antra_fun():
    print("Antras tekstas.\n")

def trecia_fun():
    pirma_fun()
    antra_fun()

trecia_fun()
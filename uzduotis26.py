# Pabandykite parašyti bent dvi pasirinktas funkcijas, kuriose būtų naudojami default parametrai. 
# Iškvieskite šias funkcijas įvairiais būdais (perduodant visus argumentus, bei neperduodant tų kuriuos galima praleisti 
# (turinčius default reikšmes)).

def info(skc1, skc2, skc3=2):
    return skc1 + skc2 - skc3

print(info(1, 1, 4))
print(info(1, 2))

def info2(vardas, pavarde, adresas="nenurodyta"):
    return vardas, pavarde, adresas

print(info2("Arnoldas", "Voiskunovic"))
print(info2("Jonas", "Jonaitis", "Seskine"))
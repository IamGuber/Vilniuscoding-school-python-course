# Susikurkite sąrašą įvykusių klaidų kodams saugoti ir užpildykite šį masyvą duomenimis. 
# Tuomet išveskite visas sukauptas klaidas administratoriui, taip, kad jis suprastų kas per klaidos įvyko. 
# Pavyzdžiui, jeigu yra kodas "ui87", tai kad išvestų "Grafinės sąsajos klaida navigacijoje", arba jeigu kodas "sys12", 
# tuomet "Trūksta operatyviosios atminties sistemoje" ir pan.

sarasas = ["error43", "error12", "error74", "error3"]

print("Ivyko sios klaidos:")

if "error43" in sarasas:
    print(sarasas[0], "- skaiciavimo klaida.")

if "error12" in sarasas:
    print(sarasas[1], "- procesoriaus klaida.")

if "error74" in sarasas:
    print(sarasas[2], "- monitoriaus kalida.")

if "error3" in sarasas:
    print(sarasas[3], "- atminties klaida.")
# Susikurkite vieną ar kelis objektus ir išmėginkite visus prieš tai pamatytus dict metodus (clear, copy, update, fromkeys, pop, …)

info = {
    "failas" : "pdf",
    "dydis" : 100,
    "kiekis" : 2
}
kopija = info.copy()
info.clear()
print(info, kopija)

naujas = {}
naujas.update(kopija)
kopija["kiekis"] = 10
info["smart"] = True
info["name"] = "failas"
kopija.pop("dydis")
info.pop("smart")
naujas.popitem()
print(info, kopija, naujas)

print( {}.fromkeys("pavarde", "jokubaitis"))
print( {}.fromkeys(["pavarde"], "jokubaitis"))
print( {}.fromkeys(["Vardai"], ["Jonas", "Povilas", "Ronaldo"]))
print( {}.fromkeys(["Vienas", "Du", "Trys"], "Pirmas"))
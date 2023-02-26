# Susikurkite vieną keletą failų, pamėginkite juos nuskaityti taikant įvairas metodikas 
# (viską vienu metu, po atskirą eilutę, sudedant į dictionary, ir pan.).

failas = open("/Users/guber/Desktop/python mokymai/19-darbas-su-failais/kazkoks-naujas.txt")
nuskaitymas = failas.read()
print(nuskaitymas)

print()
failas.seek(0)
pirma_eilute = failas.readline()
print(pirma_eilute)

print()
failas.seek(0)
testas = failas.readline(11)
print(testas)
testas2 = failas.readlines()
print(testas2)

failas.seek(0)

sarasas = list(failas.readlines())
n_sarasas = [eile.rstrip("\n") for eile in sarasas]
print(sarasas)
print(n_sarasas)
failas.close()
failas.closed

n2_sarasas = []
with open("/Users/guber/Desktop/python mokymai/19-darbas-su-failais/kazkoks-naujas.txt") as failas:
    for i in failas:
        i = i.rstrip("\n")
        redag = i.split(";")
        redag2 = dict(
            pirmas = redag[0],
            antras = redag[1],
        )
        n2_sarasas.append(redag2)

print(n2_sarasas)
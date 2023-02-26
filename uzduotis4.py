# Paprašykite vartotojo įvesti vardą, amžių, ūgį (metais) (nepamirškite ką reikia iškonvertuoti iš str į int ar float). Išveskite gautus duomenis ir jų tipus.

print("Iveskite(po kiekvieno ivedimo spaudziam ENTER) savo varda, amziu ir ugi(metrais): ")

vardas = str(input())
amzius = int(input())
ugis = float(input())

print("Jusu vardas: ", vardas, type(vardas))
print("Jusu amzius: ", amzius, type(amzius))
print("Jusu ugis: ", ugis, type(ugis))
# Susikurkite norimą sąrašą su duomenimis. Išveskite šį sąrašą šiais pavidalais:
# Kiekvieną elementą atskirant kableliu ir tarpu: pirmas, antras, trečias, …
# Kiekvieną elementą atskiriant vertikaliu brūkšneliu: pirmas|antras|trečias|...
# Kiekvieną elementą atskiriant tarpu: pirmas antras trečias

sarasas = ["python", "web", "py", "pdf", "txt"]

unpacking = ", ".join(sarasas)
print(unpacking)
unpacking = "|".join(sarasas)
print(unpacking)
unpacking = " ".join(sarasas)
print(unpacking)
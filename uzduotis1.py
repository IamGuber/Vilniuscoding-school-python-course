# Suskaičiuoti kiek duonos kepalų kepykla sugebės iškepti per dieną, ar spės įgyvendinti visus dienos užsakymus ir suskaičiuoti kiek iš jų uždirbs pelno.

darbo_valandos = 8

kepalu_per_1val = int(input("Iveskite kiek darbuotojas gali iskepti kepalu per valanda: "))
darbuotoju_kiekis = int(input("Iveskite kiek darbuotoju turi kepykla: "))
savikaina = int(input("Iveskite kokia savikaina vieno kepalo: "))
kaina = int(input("Iveskite vieno kepalo pardavimo kaina: "))
uzsakymai = int(input("Iveskite kiek kepykla tures uzsakymu per diena: "))

print()

# Suskaičiuoti kiek kepykla per vieną darbo dieną spės iškepti duonos kepalų.
kepalu_per_diena = (darbuotoju_kiekis * kepalu_per_1val) * 8
print("Per viena darbo diena kepykla iskeps:", kepalu_per_diena, "kepalu.")

# Apskaičiuoti visų kepalų savikainą, gautas pajamas pardavus ir iš to gauto pelno dalį.
# (Papildomai) Įvertinkite tai, kad pajamas ir pelną galite gauti tik iš parduotų kepalų.
pelnas_is_pagamintu = (kaina - savikaina) * kepalu_per_diena
pelnas_is_uzsakymu = (kaina - savikaina) * uzsakymai
if uzsakymai > kepalu_per_diena:
    print("Iskeptu kepalu per diena savikaina:", savikaina * kepalu_per_diena)
elif uzsakymai < kepalu_per_diena:
    print("Iskeptu kepalu per diena savikaina:", savikaina * uzsakymai)
if uzsakymai > kepalu_per_diena:
    print("Gautos pajamos is visu per diena parduotu kepalu:", kepalu_per_diena * kaina)
elif uzsakymai < kepalu_per_diena:
    print("Gautos pajamos is visu per diena parduotu kepalu:", uzsakymai * kaina)
if uzsakymai > kepalu_per_diena:
    print("Dienos pelnas:", pelnas_is_pagamintu)
elif uzsakymai < kepalu_per_diena:
    print("Dienos pelnas:", pelnas_is_uzsakymu)

# Patikrinti ar kepykla spės iškepti visus tos dienos užsakymus. Jei ne, suskaičiuoti kiek kepalų nespės iškepti.
trukumas = uzsakymai - kepalu_per_diena
if uzsakymai == kepalu_per_diena:
    print("Kepykla iskeps visus uzsakymus.")
elif trukumas < 0:
    print("Kepykla iskeps visus uzsakymus.")
else:
    print("Iki tikslo truksta:", trukumas, "kepalu.")

# Susikurkite sąrašą sandėlio likučiams saugoti (kiekvienas atskiras narys sąraše yra atskiros prekės likutis). 
# Su kiekvienu likučiu paskaičiuokite per kiek dienų bus išpirktas, jei per dieną vidutiniškai yra nuperkami 5 vnt. 
# Išveskite atsakymus atskirose eilutėse, nurodant kiek yra dabar ir kiek dienų užteks jo. 
# Pavyzdžiui, jeigu yra likučiai 74, 54 ir 32, tai 74 vnt. prekės užteks maždaug 15 dienų, 54 vnt. 
# prekės užteks maždaug 11 dienų ir t.t. Pabandykite papildyti programą taip, kad į atskirą sąrašą atrinktų tas prekes, 
# kurių užteks savaitei ar mažiau, jas išveskite atskirai, pačioje pabaigoje.

sarasas = [44, 14, 33, 13, 55, 15, 66, 16]
uzteks_sav = []

for preke in sarasas:
    for dienos in range(1, 8):
        if preke - (dienos * 5) < 0 and preke - (dienos * 5) >= -5:
            uzteks_sav.append(preke)
    for men in range(1, 31):
        if preke - (men * 5) < 0 and preke - (men * 5) >= -5:
            print(preke, "vienetu sandelyje.", preke, "sitos prekes uzteks", men, "dienom.")

print()
print("Situ prekiu uzteks savaitei arba maziau:")
print(uzteks_sav)
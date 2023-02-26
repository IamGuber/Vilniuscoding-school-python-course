# Susikurkite funkciją, kuri per argumentus gautų skaičių. Ji turėtų patikrinti ar šis skaičius yra pirminis 
# (grąžina True jei pirminis, ir False jei ne pirminis). Už funkcijos ribų sukite ciklą nuo 2 iki 15, 
# kiekvienoje ciklo iteracijoje išveskite tikrinamą skaičių ir šalia jo iškviestos funkcijos atsakymą (pvz 10 false, 11 true, ...).


def info(skaicius):
  for x in range(2,skaicius):
    if (skaicius % x) == 0:
      return f"{skaicius} {False}"
  return f"{skaicius} {True}"


for i in range(2, 15):
    print(info(i))
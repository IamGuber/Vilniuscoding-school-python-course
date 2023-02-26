# Pamėginkite išvesti skirtingą informaciją į keletą atskirų failų. 
# Tiek perrašant kas yra tame faile, tiek bandant jį papildyti. Galite išvesti kokių nors skaičiavimų informaciją.

with open("/Users/guber/Desktop/python mokymai/19-darbas-su-failais/rasymas.txt", "w") as failas:
    failas.write("Labas naujas failas!")

with open("/Users/guber/Desktop/python mokymai/19-darbas-su-failais/rasymas2.txt", "a") as failas:
    failas.write("Pirma eilute. \n")
    failas.write(f"4 + 4 = {4+4}")
# Susikurkite list pažymiams saugoti. Pamėginkite sukurti programą, kur vartotojas galėtų suvesti norimą kiekį naujų duomenų. 
# Galiausiai išveskite visus pažymius ir jų kiekį.

pazymiai = []
print('Iveskite studento pazymius per Enter. Norint baigti ivedineti iveskite "0"')
pazymys = -1

while pazymys != 0:
    pazymys = int(input("Iveskite pazymi: "))
    pazymiai.append(pazymys)

pazymiai.remove(0)

print(pazymiai)
print(len(pazymiai))
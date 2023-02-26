# Susikurkite studentų pažymių sąrašą ir užpildykite duomenimis. 
# Jeigu studentas turi neigiamų pažymių (1, 2, 3, arba 4), išveskite kiek tokių pažymių jis turi.

pazymiai = [10, 6, 4, 2, 8, 6]

pazymiai.append(3)

skc1 = pazymiai.count(1)
skc2 = pazymiai.count(2)
skc3 = pazymiai.count(3)
skc4 = pazymiai.count(4)

suma = skc1 + skc2 + skc3 + skc4

print(suma)
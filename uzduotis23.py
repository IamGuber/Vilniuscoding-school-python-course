# Susikurkite pažymių sąrašą ir užpildykite jį informacija. Surikiuokite pažymius nuo didžiausio iki mažiausio. 
# Išveskite visus turimus pažymius atskirose eilutėse. Prie kiekvieno pažymio taip pat prirašykite "puikiai", 
# jeigu jis yra 10, "labai gerai", jeigu jis yra 9 ir t.t.

pazymiai = [6, 10, 4, 8, 5, 9, 2, 11]

pazymiai.sort()
pazymiai.reverse()

for i in pazymiai:
    if i == 10:
        print(i, "Puiku!")
    elif i >= 8:
        print(i, "Labai gerai!")
    elif i >= 6:
        print(i, "Gerai.")
    elif i >= 4:
        print(i, "Pakankamai.")
    elif i >= 0:
        print(i, "Neigiamai!")
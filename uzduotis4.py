# Susikurkite miestų sąrašą. Į šį list pridėkite duomenų kurdami patį list. 
# Toliau sukurkite galimybę vartotojui papildyti list. Išveskite tiek pradinį list, tiek papildytą duomenimis. 
# Pamėginkite papildyti programą, kad vartotojas galėtų pasirinkti į kurią list vietą būtų įrašytas naujas miestas.

miestai = []
miestai.append("Vilnius")
miestai.append("Kaunas")
miestai.append("Klaipeda")

print(miestai)

naujas_miestas = input("Papildykite sarasa. Iveskite miesta: ")
saraso_vieta = int(input("Iveskite skaiciu i kuria vieta norite priedeti nauja miesta: "))
miestai.insert(saraso_vieta - 1, naujas_miestas)

print(miestai)
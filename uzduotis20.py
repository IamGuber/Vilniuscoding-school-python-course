# (sunkesnė) Parašyti for ciklą, kuris išvestų norimą kiekį fibonačiaus skaičių į ekraną. 
# Fibonačiaus sekoje kiekvienas skaičius yra lygus prieš jį ėjusių dviejų skaičių sumai: 1, 1, 2, 3, 5, 8, 13, 21…
# Susikurkite tris sveikųjų skaičių kintamuosius, kurie jums padės tai pasiekti.
# Pirmi du kintamieji saugos paskutinius du skaičius.
# Trečiasis bus šių pirmų dviejų skaičių suma.
# Pirmus du skaičius išveskite ne cikle, o prieš jį ir ciklą pradėkite vykdyti nuo 2, o ne nuo 0.
# Kiekvieno ciklo metu turite perskaičiuot trečiąjį skaičių (pirmų dviejų skaičių sudėtis), 
# tuomet pirmasis skaičius yra lygus antram, o antrasis lygus trečiam, išvesti į ekraną trečią skaičių.

ciklas = int(input("Iveskite iki kokio kieko fibonaciaus skaiciu norite matyti?: "))
skc1 = 1
skc2 = 1
print(skc1)
print(skc2)

for skaiciavimas in range(2, ciklas):
    skc3 = skc1 + skc2
    skc1 = skc2
    skc2 = skc3
    skc3 = skc1 + skc2
    print(skc3)

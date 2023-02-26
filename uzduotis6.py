# Sukurkite savo norimą dictionary(-us). Kiekviename sudėkite bent 5 savybes su reikšmėmis (reikšmes galite įdėti ir atskirai). 
# Išveskite informaciją. Pagalvokite ką dar galite su šiuo dictionary atlikti (paskaičiuoti ir pan.) ir tai padarykite.

info = {
    "gimnazija2020" : {
        "mokiniu" : 98,
        "mokytoju" : 14,
        "klasiu" : 20,
        "pamoku" : 16
    },
    "gimnazija2021" : {
        "mokiniu" : 117,
        "mokytoju" : 12,
        "klasiu" : 24,
        "pamoku" : 18
    },
    "gimnazija2022" : {
        "mokiniu" : 145,
        "mokytoju" : 23,
        "klasiu" : 28,
        "pamoku" : 27
    }
}

for i in info:
    print(i, info[i])

mokiniai = info["gimnazija2020"]["mokiniu"] + info["gimnazija2021"]["mokiniu"] + info["gimnazija2022"]["mokiniu"]
vid_mok = mokiniai / len(info)
print("Bendrai per 3 metus moykloje buvo", mokiniai, "mokiniu.")
print("Vidutiniskai per metus mokosi", vid_mok, "mokiniu.")

if info["gimnazija2020"]["mokiniu"] > info["gimnazija2021"]["mokiniu"] and info["gimnazija2020"]["mokiniu"] > info["gimnazija2022"]["mokiniu"]:
    print("Daugiausiai mokiniu mokesi 2020 metais.")
if info["gimnazija2020"]["mokiniu"] < info["gimnazija2021"]["mokiniu"] and info["gimnazija2021"]["mokiniu"] > info["gimnazija2022"]["mokiniu"]:
    print("Daugiausiai mokiniu mokesi 2021 metais.")
if info["gimnazija2022"]["mokiniu"] > info["gimnazija2021"]["mokiniu"] and info["gimnazija2020"]["mokiniu"] < info["gimnazija2022"]["mokiniu"]:
    print("Daugiausiai mokiniu mokesi 2022 metais.")


# Susikurkite funkciją kuri per argumentus priimtų pažymių masyvą. 
# Ji turėtų patikrinti ar visi pažymiai teigiami: jei visi teigiami turėtų grąžintų True kaip atsakymą, 
# o jei yra bent vienas neigiamas - False. Susikurkite du pažymių masyvus. 
# Iškvieskite šią funkciją du kartus, abu kartus perduodant skirtingus masyvus. 
# Gautus atsakymus paverskite į tekstą (jeigu gavote True - išveskite tekstą 'visi studento pažymiai teigiami', 
# jei False - 'studentas turi bent vieną neigiamą pažymį'). Šiam iškonvertavimui iš True/False į tekstą 
# galite pamėginti pasikurti atskirą funkciją, jai perduoti kitos funkcijos atsakymą.


def info(pazymiai):
    for i in pazymiai:
        if i < 5:
            return False
    return True 


sarasas1 = [10, 5, 7, 5, 8, 10]
sarasas2 = [9, 7, 9, 10, 4, 5]


def isvedimas(pazymiai):
    if info(pazymiai) == True:
        print("Visi studento pazymiai teigiami.")
    elif info(pazymiai) == False:
        print("Studentas turi bent viena neigiama pazymi.")


isvedimas(sarasas1)
isvedimas(sarasas2)
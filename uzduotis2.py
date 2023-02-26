# Susikurkite tuple iš mėnesių pavadinimų. 
# Susikurkite kitus tuples sezonams apibūdinti: žiema, pavasaris, vasara, ruduo. 
# Panaudokite slicing [start:end], kad atitinkamus mėnesius sudėtumėte į atitinkamus sezonų tuples. 
# Šį priskyrimą turite atlikti kuriant individualius sezonų tuples, kitaip išmes klaidą, kad jo negalite modifikuoti.

menesiai = ("sausis", "vasaris", "kovas", "balandis", "geguze", "birzelis", 
"liepa", "rugpjutis", "rugsejis", "spalis", "lapkritis", "gruodis")

ziema = (menesiai[0], menesiai[1], menesiai[-1])
print(ziema)

pavasaris = (menesiai[2:5])
print(pavasaris)

vasara = (menesiai[5:8])
print(vasara)

ruduo = (menesiai[8:11])
print(ruduo)
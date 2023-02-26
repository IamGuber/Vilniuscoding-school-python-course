# Įsivaizduokite, kad sukūrėte balsavimo formą, kurioje žmogus galėjo rinktis 1 iš kelių galimų 
# variantų (ar įrašyti savo) ir turite sąraše visus tuos balsavimo duomenis 
# (pvz: balsavimui panaudotas klausimas “labiausiai patinkanti kalba:”, o atsakymai 
# [‘c++’, ‘python’, ‘python’, ‘javascript’, ‘python’, ‘c#’, ‘javascript’]). 
# Atrinkite visus skirtingus atsakymų variantus į atskirą sąrašą (būtų [‘c++’, ‘python’, ‘javascript’, ‘c#’]).

info = ["c++", "python", "python", "javascript", "python", "c#", "javascript"]

print(set(info))
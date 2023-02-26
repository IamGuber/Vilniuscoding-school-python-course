# Su for pagalba, pamėginkite išvesti tokią eglutę:
# *
# **
# ***
# ****
# *****
# (papildomai) leiskite vartotojui pasirinkti kokio dydžio eglutė turėtų būti išvesta.

aukstis = int(input("Iveskite skaiciais eglutes aukstus: "))

for x in range(aukstis + 1):
    print(f"*" * x)
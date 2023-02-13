# kasse program
penger_på_konto = 2000
vare_pris = 500
if penger_på_konto < vare_pris:
    print("ikke nok penger!")
else:
    penger_på_konto = penger_på_konto - vare_pris
    print("kjøpt!")



# Alkohol sjekke program
alder = 19
if alder >= 20:
    print("Kan kjøpe alkohol over 22%")
elif alder >= 18:
    print("Kan kjøpe alkohol opptil 22%")


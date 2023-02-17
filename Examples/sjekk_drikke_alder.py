def sjekk_drikke_alder(alder):
    if alder >= 20:
        print("Kan kjøpe alkohol over 22%")
    elif alder >=18:
        print("Kan kjøpe alkohol opptil 22%")
    else:
        print("Kan ikke kjøpe alkohol")

sjekk_drikke_alder(18)
sjekk_drikke_alder(12)
sjekk_drikke_alder(76)
sjekk_drikke_alder(23)
sjekk_drikke_alder(15)
sjekk_drikke_alder(98)
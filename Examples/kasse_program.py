def kan_kjøpe_vare(vare_pris, penger_på_konto):
    if vare_pris > penger_på_konto:
        print("Kan Ikke kjøpe varen. Ikke nok penger på konto")
    else:
        print("Kan kjøpe varen! Saldo på konto etter kjøp vil være: ", penger_på_konto-vare_pris)
kan_kjøpe_vare(500, 2000)
kan_kjøpe_vare(100, 223)
kan_kjøpe_vare(20000, 100)
kan_kjøpe_vare(50, 230)
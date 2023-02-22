def ta_inn_data_fra_bruker():
    print("Velkommen til Enron sitt nye HR system!")
    navn = input("Hva er ditt navn?\n")
    årslønn = int(input("Hva er din årslønn?\n"))
    ønsket_lønn = int(input("Hva er din ønsketet lønn?\n"))
    fødsels_år = int(input("Hvilket år var du født?\n"))
    hypotetisk_spørsmål = input("Rent hypotetisk, hadde du vært ok med å hjelpe i litt regnskapssvindel? Bare svar Ja eller Nei\n")
    sjekk_ansatt_sin_alder(fødsels_år)
    regn_ut_lønn(årslønn)
    sjekk_lønnsøkning(årslønn,ønsket_lønn,hypotetisk_spørsmål)

def sjekk_ansatt_sin_alder(fødselsår):
    nåværende_år = 1997
    alder = nåværende_år - fødselsår
    if alder < 18:
        print("Du er altfor ung til å jobbe for Enron!")
        quit()
    elif alder > 100:
        print("Ey! Dette er ikke et gamlehjem! Stikk!")
        quit()
    else:
        print("Din alder",alder, "er helt perfekt for Enron!")

def regn_ut_lønn(årslønn):
    måneds_lønn = årslønn / 12
    uke_lønn = årslønn / 52
    dags_lønn = uke_lønn / 5
    time_lønn = dags_lønn / 7.5
    print("Månedslønn:",måneds_lønn)
    print("ukelønn:",uke_lønn)
    print("dagslønn:",dags_lønn)
    print("timelønn:",time_lønn)

def sjekk_lønnsøkning(årslønn, ønsket_lønn, hypotetisk_spørsmål):
    if årslønn == ønsket_lønn:
        print("Din lønn blir ikke endret, fordi du alerede tjener det du har lyst på!")
    elif årslønn > ønsket_lønn:
        print("Vi ser at du ønsker deg mindre lønn enn det du tjener, derfor justere vi din lønn ned til å møte dine ønsker!🎊")
    else:
        if hypotetisk_spørsmål.lower() == "ja":
            print("Du er en fantastisk ansatt! Vi vil derfor gjerne øke din lønn fra", årslønn, "til", ønsket_lønn,"🥳💰")
        else:
            print("huff... jeg ser at du var 27 sekunder for sein på jobb den 12 desember 1992, derfor kan vi ikke gi det høyere lønn. Prøv å jobb hardere neste gang!")

ta_inn_data_fra_bruker()
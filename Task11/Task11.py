# call the sjekk_lønn and print_fakta functions using data from the user.

def print_fakta(navn,alder,stilling,nåværende_lønn,ønsket_lønn):
    print("Mitt navn er", navn, "Jeg er", alder, "år gammel, min stilling i PIT er", stilling, "min nåværende lønn er", nåværende_lønn, "men, jeg ønsker en lønn på", ønsket_lønn)
    print(navn, "25 år, Utvikler hos PIT")
    print(navn, "driver med hacking på fritiden")
    print(navn, "har vært top 500 i overwatch i Europa")
    print(navn, "er brunt belte i krav maga")
    print(navn, "har spilt i korps i over 10 år")
    print(navn, "liker å trene")
def sjekk_lønn(age,nåværende_lønn, ønsket_lønn):
    if age >= 18:
        if nåværende_lønn > ønsket_lønn:
            print("Perfekt!")
        elif nåværende_lønn == ønsket_lønn:
            print("Det kan bli bedre")
        else:
            print("😠")

def ta_inn_data_fra_bruker():
    navn = input("Hva er ditt navn?\n")
    alder = input("Hvor gammel er du?\n")
    stilling = input("Hva er din stilling\n")
    nåværende_lønn = input("Hva er din nåværende lønn?\n")
    ønsket_lønn = input("Hvor mye ønsker du at du hadde i lønn?\n")

    sjekk_lønn(alder,nåværende_lønn,ønsket_lønn)
    print_fakta(navn,alder,stilling,nåværende_lønn,ønsket_lønn)

ta_inn_data_fra_bruker()

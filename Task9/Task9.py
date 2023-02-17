# Convert your "sjekk_lønn" function to take in the following arguments:
# age, nåværende_lønn and ønsket_lønn

navn = "Martin"
age = 25
stilling = "Utvikler"
nåværende_lønn = 700000
ønsket_lønn = 10000000

def print_fakta(navn,alder,stilling,nåværende_lønn,ønsket_lønn):
    print("Mitt navn er", navn, "Jeg er", age, "år gammel, min stilling i PIT er", stilling, "min nåværende lønn er", nåværende_lønn, "men, jeg ønsker en lønn på", ønsket_lønn)
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

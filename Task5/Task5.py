# Good job! You have added your first control logic.
# Now, expand this, we only want to check people that are adults, aka have an age greater or equal to 18.

navn = "Martin"
age = 25
stilling = "Utvikler"
nåværende_lønn = 700000
ønsket_lønn = 10000000

print("Mitt navn er",navn,"Jeg er", age, "år gammel, min stilling i PIT er", stilling,"min nåværende lønn er",nåværende_lønn,"men, jeg ønsker en lønn på",ønsket_lønn)
print(navn, "25 år, Utvikler hos PIT")
print(navn, "driver med hacking på fritiden")
print(navn, "har vært top 500 i overwatch i Europa")
print(navn, "er brunt belte i krav maga")
print(navn, "har spilt i korps i over 10 år")
print(navn, "liker å trene")


if(age >= 18):
    if nåværende_lønn > ønsket_lønn:
        print("Perfekt!")
    elif nåværende_lønn == ønsket_lønn:
        print("Det kan bli bedre")
    else:
        print("😠")
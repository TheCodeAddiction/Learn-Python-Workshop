# We have made some pretty cool prints, now let's play with some control logic, aka: Rules or normes
# make two variables, one containing your desired salary and the other containing your current salary
# use if else statements to check if your current salary matches your desired salary

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


if nåværende_lønn > ønsket_lønn:
    print("Veldig fornøyd!")
elif nåværende_lønn == ønsket_lønn:
    print("Fornøyd")
else:
    print("😠")
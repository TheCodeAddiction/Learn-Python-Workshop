# Python Cheatsheet

---
### Variabler
Format: `variable_navn = data`

####F.eks:
* Lage variable som holder på tekst: `navn = "Martin"`
* Lage variable som holder på tallalder: `alder = 12`
* Lage variable som holder på en liste av tekst: `list_med_navn = ["Martin","Marianne","Bob"]`
* Lage variable som holder på en liste med tall: `list_med_alder = [12,24,68,13,5]`
---
### Funksjoner
**Lag din egen funksjon format:**
```
def funksjons_navn(argument1, argument2):
    <din kode her>
```
####F.eks:
```
def plus_sammen_to_tall(tall1, tall2):
    print(tall1 + tall2)
```
**Note:** Du behøver ikke å bruke argumenter, f.eks:
```
def print_hallo():
    print("hey!")
```

**Kall en funksjon / bruke en funksjon:**

Syntaks: `funksjon_navn()`
####F.eks:
```
def print_hallo(): <-- lag en funksjon
    print("hey!")
    
print_hallo() <-- bruk / kall funksjonen
```
---
### Kontroll logikk
Format: 
```
if betingelse:
    din_kode_her
elif betingelse:
    din_kode_her
else:
    din_kode.her
```
####F.eks:
````
if alder >= 20:
    print("Kan kjøpe alkohol over 22%")
elif alder >=18:
    print("Kan kjøpe alkohol opptil 22%")
else:
    print("Kan ikke kjøpe alkohol")
````
---
###Spesifiser datatype:
* For å tolke en variable som tekst: `str(variable_navn)`
* For å tolke en variable som tall: `int(variable_navn)`
---
###Loops
#### while loop format:
```
while tilstand:
    din_kode_her
```
**f.eks**
````
while 1=1:
    print("hey!")
````
````
while True:
    print("hey!")
````
#### For loop format:
````
for variable_navn in liste:
    din_kode_her
````
**f.eks**
````
liste_med_frukt = ["apple", "banana", "cherry"]
for frukt in liste_med_frukt:
  print(x)
````
---
###Ta inn data fra terminal
Format: `variable = input("tekst som bruker ser")`

**f.eks**
`navn = input("hva er ditt navn? ")`

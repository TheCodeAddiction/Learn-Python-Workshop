# Premis
Året er 1997 og du jobber som systemutvikler for det store og lukseriøse energi firmaet Enron.

Din team leder har bedt deg om å utvikle et HR system for de ansatte. System har
følgene krav:
1. Systemet skal ta inn følgene data fra en ansatt:
   2. Navn
   3. årslønn
   4. ønsketlønn
   5. hvilket år de var født i (du behøver ikke å ta inn datoen, kun årstallet.)
   6. Om de, hypotetisk, er ok med å hjelpe firmaet med litt "regnskapssvindel", spørsmålet er, selvfølgelig kun hyptotetisk. Svaret skal være et "ja" eller "nei"
---
2. Programet skal ha en funksjon, som regner ut alder til den ansatte. Dette gjør du ved å ta
det nåværende året (`1997`) og trekker fra den ansattes fødelesår.
   3. Hvis en person er under 18, eller over 100, skal du gi dem en beskjed at de enten er
   for ung, eller for gammel til å jobbe for Enron og så avslutte programmet ved å bruke `quit()` funkjonen.
---
3. Du skal lage en funksjon som regner ut den ansattes, måned, uke, dags og timelønn, basert på årslønnen de oppgir.
---
4. Du skal lage en funksjon som sjekker om den ansatte skal få endre sin nåværendelønn, til den lønnen de har lyst på. 
   6. Hvis de alerede tjener det de ønsker å tjene, skal du fortelle dem at de alerede tjener det de ønsker.
   7. Hvis de tjener mer enn det de ønsker å tjene, skal du med glede informere dem om at du har redusert deres lønn slik at den matcher
   deres "ønsket inntekt".
   8. Hvis de tjener mindre enn det de ønsker, skal du sjekke om den ansatte, har svart "ja" eller "nei" på det hypotetiske spørsmålet
   angående "regnskapssvindel". Hvis de svarte "ja", gir du dem lønnøkningen fordi de er flink ansatte (helt urelatert til at de svarte ja)
   Hvis de svarte "nei" må de finne på en god unskyldning til hvorfor de ikke fikk lønnøkningen.
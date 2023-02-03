class Ansatt:
    navn = ""
    alder = 0
    stilling = ""
    inntekt = 0
    # NOTE: "self" is gonna confuse people
    def __int__(self, navn, alder, stilling, inntekt):
        self.navn = navn
        self.alder = alder
        self.stilling = stilling
        self.inntekt = inntekt

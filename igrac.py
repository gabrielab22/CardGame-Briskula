import random


class Igrac:

    def __init__(self, ime):
        self.ime = ime

    def akcija(self, stanje_igre):
        index = random.choice([x for x in range(len(stanje_igre["ruka"].karte))])
        return index




from random import shuffle


# igraca karta
class Karta:
    Slika = {1: "A", 2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7", 11: "J", 12: "Q", 13: "K"}

    def __init__(self, broj, zog):
        self.broj, self.zog = broj, zog

    def __str__(self):
        return "[" + Karta.Slika[self.broj] + self.zog + "]"


# kolekcija karata
class Karte:

    def __init__(self, karte):
        self.karte = karte

    def __str__(self):
        return " ".join(str(k) for k in self.karte)

    def dodaj(self, k):
        self.karte += [k]

    def izvuci(self, i):
        k, self.karte = self.karte[i], self.karte[:i] + self.karte[i + 1:]
        return k


# zamijesani spil od 40 karata
class Spil(Karte):

    def __init__(self):
        super().__init__([Karta(b, z) for b in [1, 2, 3, 4, 5, 6, 7, 11, 12, 13] for z in ["D", "K", "S", "B"]])
        shuffle(self.karte)

    def peskaj(self):
        return self.izvuci(0)


if __name__ == "__main__":
    pass


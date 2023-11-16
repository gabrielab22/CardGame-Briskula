from main import Karte, Spil
from igrac import Igrac
from human import Human


class Briskula:

    def __init__(self, igrac1, igrac2):

        self.bodovi = {1: 11, 2: 0, 3: 10, 4: 0, 5: 0, 6: 0, 7: 0, 11: 2, 12: 3, 13: 4}
        self.snaga = {1: 9, 2: 0, 3: 8, 4: 1, 5: 2, 6: 3, 7: 4, 11: 5, 12: 6, 13: 7}

        # inicijalizacija
        self.igrac1 = igrac1 if igrac1.prvi_po_redu else igrac2
        self.igrac2 = igrac2 if igrac1.prvi_po_redu else igrac1
        self.red = 1
        self.spil = Spil()
        self.igrac1.dobivene = Karte([])
        self.igrac2.dobivene = Karte([])
        self.igrac1.ruka = Karte([self.spil.peskaj() for x in range(3)])
        self.igrac2.ruka = Karte([self.spil.peskaj() for x in range(3)])
        self.briskula = self.spil.peskaj()
        self.spil.dodaj(self.briskula)
        self.stol = Karte([])

    def __str__(self):
        print("Broj karata u spilu: ", len(self.spil.karte))
        print("Briskula: ", self.briskula)
        print("Karte na stolu: ", self.stol)
        print("Karte igraca 1: ", self.igrac1.ruka)
        print("Karte igraca 2: ", self.igrac2.ruka)

    def rezultat(self):
        rezultat_1 = 0
        for karta in self.igrac1.dobivene.karte:
            rezultat_1 += self.bodovi[karta.broj]
        rezultat_2 = 0
        for karta in self.igrac2.dobivene.karte:
            rezultat_2 += self.bodovi[karta.broj]
        if rezultat_1 > rezultat_2:
            return 1
        if rezultat_2 > rezultat_1:
            return 2
        return 0

    def pobjednik_ruke(self, karta1, karta2):
        if karta1.zog == self.briskula.zog:
            if karta2.zog == self.briskula.zog:
                if self.snaga[karta1.broj] > self.snaga[karta2.broj]:
                    return 1
                else:
                    return 2
            else:
                return 1
        if karta2.zog == self.briskula.zog:
            return 2
        if karta1.zog == karta2.zog:
            if self.snaga[karta1.broj] > self.snaga[karta2.broj]:
                return 1
            else:
                return 2
        return 1

    def stanje(self, red):
        stanje_dict = {
            "briskula": self.briskula,
            "ruka": self.igrac1.ruka if red == 1 else self.igrac2.ruka,
            "stol": self.stol,
            "dobivene": self.igrac1.dobivene if red == 1 else self.igrac2.dobivene,
            "dobivene protivnik": self.igrac2.dobivene if red == 1 else self.igrac1.dobivene,
        }
        return stanje_dict

    def odigraj_ruku(self, prikaz=False):
        if self.red == 1:
            index1 = self.igrac1.akcija(self.stanje(1))
            karta1 = self.igrac1.ruka.izvuci(index1)
            index2 = self.igrac2.akcija(self.stanje(2))
            karta2 = self.igrac2.ruka.izvuci(index2)
            pobjednik = self.pobjednik_ruke(karta1, karta2)
            if pobjednik == 1:
                self.igrac1.dobivene.dodaj(karta1)
                self.igrac1.dobivene.dodaj(karta2)
            else:
                self.igrac2.dobivene.dodaj(karta1)
                self.igrac2.dobivene.dodaj(karta2)
                self.red = 2
        else:
            index1 = self.igrac2.akcija(self.stanje(2))
            karta1 = self.igrac2.ruka.izvuci(index1)
            index2 = self.igrac1.akcija(self.stanje(1))
            karta2 = self.igrac1.ruka.izvuci(index2)
            pobjednik = self.pobjednik_ruke(karta1, karta2)

            if pobjednik == 1:
                self.igrac2.dobivene.dodaj(karta1)
                self.igrac2.dobivene.dodaj(karta2)
                self.red = 1
            else:
                self.igrac1.dobivene.dodaj(karta1)
                self.igrac1.dobivene.dodaj(karta2)
        if prikaz:
            print(f"Pobjednik je: {str(pobjednik)} od karata {karta1} i {karta2}")
        if len(self.spil.karte) > 0:
            self.igrac1.ruka.dodaj(self.spil.peskaj())
            self.igrac2.ruka.dodaj(self.spil.peskaj())

    def odigraj_partiju(self, prikaz=True):
        for i in range(20):
            if prikaz:
                self.__str__()
            self.odigraj_ruku(prikaz)


class IgracBriskule(Igrac):

    def __init__(self, igrac, prvi_po_redu):
        super().__init__(igrac)
        self.prvi_po_redu = prvi_po_redu
        self.ruka = Karte([])
        self.dobivene = Karte([])

    def promijeni_red(self):
        self.prvi_po_redu = not self.prvi_po_redu

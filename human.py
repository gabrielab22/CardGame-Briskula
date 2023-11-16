from igrac import Igrac


class Human(Igrac):

    def akcija(self, stanje_igre):
        karta_za_odigrati = int(input("Koji redni broj karte zelite odigrati, 0, 1 ili 2?)"))
        return karta_za_odigrati

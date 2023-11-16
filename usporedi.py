from briskula import IgracBriskule, Briskula


igrac1 = IgracBriskule("Gabriela Bot", True)
igrac2 = IgracBriskule("Bot", False)
rezultat = {0: 0, 1: 0, 2: 0}
for i in range(1):
    briskula = Briskula(igrac1, igrac2)
    briskula.odigraj_partiju(True)
    print(briskula.rezultat())
    rezultat[briskula.rezultat()] += 1
print(rezultat)

igrac1.promijeni_red()
igrac2.promijeni_red()
print(igrac2.prvi_po_redu)
for i in range(1):
    briskula = Briskula(igrac1, igrac2)
    briskula.odigraj_partiju(True)
    rezultat_int = briskula.rezultat()
    rezultat_int = 1 if rezultat_int == 2 else 2 if rezultat_int == 1 else 0
    rezultat[rezultat_int] += 1

print(rezultat)

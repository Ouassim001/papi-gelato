bedrag = float(input("how much\n"))
factuurbedrag = float(input("hwo much total?\n"))

kortingperc = 6


def berekenkorting(B):
    korting = B / 100 * kortingperc
    return korting


korting = berekenkorting(bedrag)
print(korting)

factuurkorting = berekenkorting(factuurbedrag)
print(factuurkorting)
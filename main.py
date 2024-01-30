from UkladSlonecznyKlasy import CialoNiebieskie, UkladSloneczny
from UI import UkladSlonecznyUI

try:
    with open('uklad_sloneczny.txt', 'r') as plik:
        linie = plik.readlines()

    lista_cial_niebieskich = []
    for linia in linie:
        data = linia.strip().split(', ')

        nazwa = (data[0])
        masa = (float(data[1].rstrip("kg")))
        odleglosc_od_slonca = (float(data[2].rstrip("dni")))
        okres = (float(data[3].rstrip("km")))

        lista_cial_niebieskich.append(CialoNiebieskie(nazwa, masa, odleglosc_od_slonca, okres))

    uklad_sloneczny = UkladSloneczny(lista_cial_niebieskich)
except:
    Merkury = CialoNiebieskie("Merkury", 330.2, 5.8, 88)
    Wenus = CialoNiebieskie("Wenus", 4868.5, 10.8, 225)
    Ziemia = CialoNiebieskie("Ziemia", 5974.2, 14.9, 365)
    Mars = CialoNiebieskie("Mars", 641.9, 22.8, 687)
    Jowisz = CialoNiebieskie("Jowisz", 1898600.8, 77.8, 4333)
    Saturn = CialoNiebieskie("Saturn", 568516.8, 142.7, 10756)
    Uran = CialoNiebieskie("Uran", 86841, 287.1, 30707)
    Neptun = CialoNiebieskie("Neptun", 102439.6, 449.8, 60223)

    uklad_sloneczny = UkladSloneczny([Ziemia, Mars, Jowisz, Saturn, Uran, Neptun])
    uklad_sloneczny.aktualizuj_plik()
uklad_sloneczny_ui = UkladSlonecznyUI(uklad_sloneczny)
uklad_sloneczny_ui.show()
class CialoNiebieskie:
    def __init__(self, nazwa, masa, odleglosc_od_slonca, okres):
        self.nazwa = nazwa
        self.masa = masa
        self.odleglosc_od_slonca = odleglosc_od_slonca
        self.okres = okres

    def __str__(self):
        return str(self.nazwa) + ", " + str(self.masa) + "kg, " + str(self.okres) + "dni, " + str(
            self.odleglosc_od_slonca) + "km"

    def edytuj(self, nowa_nazwa, nowa_masa, nowa_odleglosc_od_slonca, nowy_okres):
            self.nazwa = nowa_nazwa
            self.masa = float(nowa_masa)
            self.odleglosc_od_slonca = float(nowa_odleglosc_od_slonca)
            self.okres = float(nowy_okres)

class UkladSloneczny:
    def __init__(self, ciala_niebieskie):
        self.ciala_niebieskie = ciala_niebieskie


    def __len__(self):
        return len(self.ciala_niebieskie)

    def __sub__(self, cialo_niebieskie):
        self.ciala_niebieskie.remove(cialo_niebieskie)
        self.aktualizuj_plik()
        print(self.ciala_niebieskie)

    def __str__(self):
        uklad_sloneczny_plik = open("uklad_sloneczny.txt", "r")
        objects = uklad_sloneczny_plik.readlines()
        uklad_sloneczny_plik.close()

        for i in range(0, len(objects)):
            objects[i] = objects[i].replace("\n", "")

        return str(objects)

    def aktualizuj_plik(self):
        uklad_sloneczny_plik = open("uklad_sloneczny.txt", "w")
        for cialo_niebieskie in self.ciala_niebieskie:
            uklad_sloneczny_plik.write(str(cialo_niebieskie) + "\n")
        uklad_sloneczny_plik.close()


    def dodaj(self, nowe_cialo_niebieskie):
        for i in self.ciala_niebieskie:
            if (
                    i.nazwa == nowe_cialo_niebieskie.nazwa
            ):
                raise ValueError("Istnieje juz taka planeta")

        self.ciala_niebieskie.append(nowe_cialo_niebieskie)
        self.aktualizuj_plik()

    def usun(self, cialo_niebieskie):
        wybrane_cialo_niebieskie = cialo_niebieskie.split(", ")

        for i in self.ciala_niebieskie:
            if (
                    i.nazwa == wybrane_cialo_niebieskie[0] and
                    str(i.masa) + "kg" == wybrane_cialo_niebieskie[1] and
                    str(i.odleglosc_od_slonca) + "km" == wybrane_cialo_niebieskie[3] and
                    str(i.okres) + "dni" == wybrane_cialo_niebieskie[2]
            ):
                self.ciala_niebieskie.remove(i)
                break
        self.aktualizuj_plik()

    def sortuj_przez(self, kryterium, sortowanie):
        if len(self.ciala_niebieskie) == 0:
            return 0

        wartosci = [getattr(cialo_niebieskie, kryterium) for cialo_niebieskie in self.ciala_niebieskie]
        min_wartosc, max_wartosc = min(wartosci), max(wartosci)

        rozmiar_zakresu = (max_wartosc - min_wartosc) / len(self.ciala_niebieskie)
        if rozmiar_zakresu == 0:
            rozmiar_zakresu = 1

        kubelki = [[] for _ in range(len(self.ciala_niebieskie) + 1)]

        for cialo_niebieskie in self.ciala_niebieskie:
            indeks_kubelka = int((getattr(cialo_niebieskie, kryterium) - min_wartosc) / rozmiar_zakresu)
            kubelki[indeks_kubelka].append(cialo_niebieskie)

        for i in range(len(kubelki)):
            kubelki[i] = sorted(kubelki[i], key=lambda x: getattr(x, kryterium))

        posortowana_lista = [cialo_niebieskie for kubelek in kubelki for cialo_niebieskie in kubelek]

        if sortowanie == "m":
            posortowana_lista = posortowana_lista[::-1]

        self.ciala_niebieskie = posortowana_lista
        self.aktualizuj_plik()
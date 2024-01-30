import tkinter as tk
import tkinter.messagebox
from UkladSlonecznyKlasy import CialoNiebieskie

class UkladSlonecznyUI:
    def __init__(self, uklad_sloneczny):
        self.uklad_sloneczny = uklad_sloneczny
        self.window = tk.Tk()
        self.window.title("Układ Słoneczny")
        self.window.geometry("300x600")
        self.rosnaco_var = tk.BooleanVar()
        self.malejaco_var = tk.BooleanVar()
        self.uklad_sloneczny = uklad_sloneczny

        nazwa_napis = tk.Label(self.window, text="Nazwa:")
        nazwa_napis.pack()
        self.nazwa_wejscie = tk.Entry(self.window, width=30)
        self.nazwa_wejscie.pack()

        masa_napis = tk.Label(self.window, text="Masa: [*10^(21)kg]")
        masa_napis.pack()
        self.masa_wejscie = tk.Entry(self.window, width=30)
        self.masa_wejscie.pack()

        odleglosc_napis = tk.Label(self.window, text="Odległość od Słońca: [*10^(7)km]")
        odleglosc_napis.pack()
        self.odleglosc_wejscie = tk.Entry(self.window, width=30)
        self.odleglosc_wejscie.pack()

        okres_napis = tk.Label(self.window, text="Okres obiegu dookoła Słońca: [dni]")
        okres_napis.pack()
        self.okres_wejscie = tk.Entry(self.window, width=30)
        self.okres_wejscie.pack()

        dodaj_przycisk = tk.Button(self.window, text="Dodaj", command=self.dodaj_obiekt)
        dodaj_przycisk.pack()

        usun_przycisk = tk.Button(self.window, text="Usuń", command=self.usun_obiekt)
        usun_przycisk.pack()

        edytuj_przycisk = tk.Button(self.window, text="Edytuj", command=self.edytuj)
        edytuj_przycisk.pack()

        sposob_napis = tk.Label(self.window, text="Sposób sortowania:")
        sposob_napis.pack()

        rosnaco_przycisk = tk.Checkbutton(self.window, text="Rosnąco", variable=self.rosnaco_var, command=self.sortuj_rosnaco)
        rosnaco_przycisk.pack()

        malejaco_przycisk = tk.Checkbutton(self.window, text="Malejąco", variable=self.malejaco_var, command=self.sortuj_malejaca)
        malejaco_przycisk.pack()

        sortowanie_napis = tk.Label(self.window, text="Sortuj według:")
        sortowanie_napis.pack()

        masa_przycisk = tk.Button(self.window, text="Masa", command=self.sortuj_po_masie)
        masa_przycisk.pack()

        okres_przycisk = tk.Button(self.window, text="Okres", command=self.sortuj_po_okresie)
        okres_przycisk.pack()

        odl_przycisk = tk.Button(self.window, text="Odległość od Słońca", command=self.sortuj_po_odl)
        odl_przycisk.pack()

        self.lista = tk.Listbox(self.window, selectmode=tk.SINGLE, width=40)
        self.lista.pack()

        for cialo_niebieskie in self.uklad_sloneczny.ciala_niebieskie:
            self.lista.insert(tk.END, str(cialo_niebieskie))

        self.lista.bind("<<ListboxSelect>>", self.lista_event)

    def sortuj_rosnaco(self):
        if self.rosnaco_var.get():
            self.malejaco_var.set(False)

    def sortuj_malejaca(self):
        if self.malejaco_var.get():
            self.rosnaco_var.set(False)

    def sortuj_po_masie(self):
        if self.malejaco_var.get():
            self.uklad_sloneczny.sortuj_przez("masa", "m")
        else:
            self.uklad_sloneczny.sortuj_przez("masa", "r")
        self.update_lista()

    def sortuj_po_okresie(self):
        if self.malejaco_var.get():
            self.uklad_sloneczny.sortuj_przez("okres", "m")
        else:
            self.uklad_sloneczny.sortuj_przez("okres", "r")
        self.update_lista()

    def sortuj_po_odl(self):
        if self.malejaco_var.get():
            self.uklad_sloneczny.sortuj_przez("odleglosc_od_slonca", "m")
        else:
            self.uklad_sloneczny.sortuj_przez("odleglosc_od_slonca", "r")
        self.update_lista()

    def update_lista(self):
        # Wyczyść aktualne elementy na liście
        self.lista.delete(0, tk.END)

        # Wstaw zaktualizowane elementy do listy
        for cialo_niebieskie in self.uklad_sloneczny.ciala_niebieskie:
            self.lista.insert(tk.END, str(cialo_niebieskie))

    def show(self):
        self.window.mainloop()

    def wyczysc_dane(self):
        self.nazwa_wejscie.delete(0, tk.END)
        self.masa_wejscie.delete(0, tk.END)
        self.odleglosc_wejscie.delete(0, tk.END)
        self.okres_wejscie.delete(0, tk.END)

    def pobierz_dane(self):
        nazwa = self.nazwa_wejscie.get()
        masa = self.masa_wejscie.get()
        odleglosc_do_slonca = self.odleglosc_wejscie.get()
        okres = self.okres_wejscie.get()
        return nazwa, masa , odleglosc_do_slonca, okres

    def sprawdz_dane(self, nazwa, masa, odleglosc_do_slonca, okres):
        if nazwa == "" or masa == "" or odleglosc_do_slonca == "" or okres == "":
            raise ValueError("Uzupelnij wszystkie pola")

        if not (masa.replace('.', '', 1).isdigit() or masa.isdigit()):
            raise ValueError("Zly typ pola: masa musi byc liczba")

        if not (odleglosc_do_slonca.replace('.', '', 1).isdigit() or odleglosc_do_slonca.isdigit()):
            raise ValueError("Zly typ pola: odleglosc od slonca musi byc liczba")

        if not (okres.replace('.', '', 1).isdigit() or okres.isdigit()):
            raise ValueError("Zly typ pola: okres musi byc liczba")

    def lista_event(self, event):
        wybrany_index = self.lista.curselection()

        if wybrany_index:
            wybrana_wartosc = self.lista.get(wybrany_index)
            wartosc_split = wybrana_wartosc.split(", ")
            self.wyczysc_dane()
            self.nazwa_wejscie.insert(0, wartosc_split[0])
            self.masa_wejscie.insert(0, wartosc_split[1][0:-2])
            self.okres_wejscie.insert(0, wartosc_split[2][0:-3])
            self.odleglosc_wejscie.insert(0, wartosc_split[3][0:-2])

    def dodaj_obiekt(self):
        try:
            nazwa, masa, odleglosc_do_slonca, okres = self.pobierz_dane()
            self.sprawdz_dane(nazwa, masa, odleglosc_do_slonca, okres)

        except ValueError as e:
            tkinter.messagebox.showinfo('Błąd', e.__str__())
            self.wyczysc_dane()
            return

        nowe_cialo_niebieskie = CialoNiebieskie(nazwa, float(masa), float(odleglosc_do_slonca), float(okres))

        try:
            self.uklad_sloneczny.dodaj(nowe_cialo_niebieskie)
        except ValueError as e:
            tkinter.messagebox.showinfo('Błąd', e.__str__())
            return

        self.lista.insert(tk.END, str(nowe_cialo_niebieskie))
        self.update_lista()
        self.wyczysc_dane()

    def usun_obiekt(self):
        try:
            wybrany_index = self.lista.curselection()
            print(wybrany_index)
            if not wybrany_index:
                raise ValueError("Wybierz pole do usunięcia")
            wybrany_obiekt = self.lista.get(wybrany_index)
            self.uklad_sloneczny.usun(wybrany_obiekt)
            print(self.uklad_sloneczny)
            if wybrany_index:
                self.lista.delete(wybrany_index)
                self.update_lista()
                self.wyczysc_dane()

        except ValueError as e:
            tkinter.messagebox.showinfo('Błąd', e.__str__())
            return

    def edytuj(self):
        try:
            wybrany_index = self.lista.curselection()
            if not wybrany_index:
                raise ValueError("Wybierz planetę do edycji")

            wybrane_cialo_niebieskie = self.uklad_sloneczny.ciala_niebieskie[wybrany_index[0]]

            edycja_okno = tk.Toplevel(self.window)
            edycja_okno.title("Edytuj obiekt")
            edycja_okno.geometry("300x200")

            nazwa_napis = tk.Label(edycja_okno, text="Nowa nazwa:")
            nazwa_napis.pack()
            nowa_nazwa_wejscie = tk.Entry(edycja_okno, width=30)
            nowa_nazwa_wejscie.pack()
            nowa_nazwa_wejscie.insert(0, wybrane_cialo_niebieskie.nazwa)  # Dodaj stare dane

            masa_napis = tk.Label(edycja_okno, text="Nowa masa: [*10^(21)]")
            masa_napis.pack()
            nowa_masa_wejscie = tk.Entry(edycja_okno, width=30)
            nowa_masa_wejscie.pack()
            nowa_masa_wejscie.insert(0, str(wybrane_cialo_niebieskie.masa))  # Dodaj stare dane

            odleglosc_napis = tk.Label(edycja_okno, text="Nowa odległość od Słońca: [km]")
            odleglosc_napis.pack()
            nowa_odleglosc_wejscie = tk.Entry(edycja_okno, width=30)
            nowa_odleglosc_wejscie.pack()
            nowa_odleglosc_wejscie.insert(0, str(wybrane_cialo_niebieskie.odleglosc_od_slonca))  # Dodaj stare dane

            okres_napis = tk.Label(edycja_okno, text="Nowy okres obiegu dookoła Słońca: [dni]")
            okres_napis.pack()
            nowy_okres_wejscie = tk.Entry(edycja_okno, width=30)
            nowy_okres_wejscie.pack()
            nowy_okres_wejscie.insert(0, str(wybrane_cialo_niebieskie.okres))  # Dodaj stare dane

            # Funkcja obsługująca zapisanie nowych danych po naciśnięciu przycisku
            def zapisz_edycje():
                try:
                    nowa_nazwa = nowa_nazwa_wejscie.get()
                    nowa_masa = nowa_masa_wejscie.get()
                    nowa_odleglosc_od_slonca = nowa_odleglosc_wejscie.get()
                    nowy_okres = nowy_okres_wejscie.get()
                    self.sprawdz_dane(nowa_nazwa, nowa_masa, nowa_odleglosc_od_slonca, nowy_okres)

                    wybrane_cialo_niebieskie.edytuj(nowa_nazwa, nowa_masa, nowa_odleglosc_od_slonca, nowy_okres)
                    self.uklad_sloneczny.aktualizuj_plik()
                    self.update_lista()   ## tutaj jest do naprawienia zeby wyswietlalo ladnie i chuj
                    edycja_okno.destroy()

                except ValueError as g:
                    tkinter.messagebox.showinfo('Błąd', g.__str__())

            zapisz_przycisk = tk.Button(edycja_okno, text="Zapisz", command=zapisz_edycje)
            zapisz_przycisk.pack()

        except ValueError as e:
            tkinter.messagebox.showinfo('Błąd', e.__str__())
            return




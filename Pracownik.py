
from tkinter import *
import tkinter as tk
import tkinter.ttk as ttk

from Klient import Klient
from bazaSamochodow import bazaSamochodow
from bazaUzytkownikow import bazaUzytkownikow
from ZarzadzajSamochodami import ZarzadzajSamochodami

class Pracownik(Klient):
    
    def __init__(self):
        self.stanowsiko = "Pracownik"

        self.okno = Tk()
        self.okno.configure(bg="#708090")
        self.okno.geometry("500x500")
        self.baza=bazaSamochodow()

        myLabel = Label(self.okno, text="Pracownik", bg="#708090")
        myLabel.pack()

        self.bazaUzytkownikow = bazaUzytkownikow()
        self.ZarzadzajSamochodami = ZarzadzajSamochodami(self.okno)
        self.bazaSamochodow = bazaSamochodow()

        przyciskWyswietleniaUzytkownikow = Button(self.okno, text="Wyswietl uzytkownikow", command=self.wyswietlUzytkownikow)
        przyciskWyswietleniaUzytkownikow.pack()

        przyciskWyswietleniaSamochodow = Button(self.okno, text="Wyswietl samochody", command=self.wyswietlSamochody)
        przyciskWyswietleniaSamochodow.pack()

        przyciskDodaniaSamochodow = Button(self.okno, text="Dodaj samochod", command=self.ZarzadzajSamochodami.dodajSamochod)
        przyciskDodaniaSamochodow.pack()
        
        przyciskUsuwaniaSamochodow = Button(self.okno, text="Usun samochod", command=self.ZarzadzajSamochodami.usunSamochod)
        przyciskUsuwaniaSamochodow.pack()

        przyciskWyswietlRezerwacje = Button(self.okno, text="Wyświetl rezerwacje", command=self.wyswietlRezerwacje)
        przyciskWyswietlRezerwacje.pack()

        przyciskWypozycz = Button(self.okno, text="Wypozycz", command=self.WypozyczSamochod)
        przyciskWypozycz.pack()

        przyciskOddaj = Button(self.okno, text="Oddaj", command=self.OddajSamochod)
        przyciskOddaj.pack()

        przyciskWyloguj = Button(self.okno, text="Wyloguj", command=self.wyloguj)
        przyciskWyloguj.pack()

        myLabell = Label(self.okno, text="Dostępne samochody:", bg="#708090")
        myLabell.pack()

        liczba = self.wyswietlSamochodyDost()
        myLabell.configure(text=f"Liczba dostępnych samochodów: {liczba}")

        myLabelR = Label(self.okno, text="Zarezerwowane samochody:", bg="#708090")
        myLabelR.pack()

        liczba = self.wyswietlSamochodyZarezerwowane()
        myLabelR.configure(text=f"Liczba zarezerwowanych samochodów: {liczba}")

        myLabelR = Label(self.okno, text="Niedostepne samochody:", bg="#708090")
        myLabelR.pack()

        liczba = self.wyswietlSamochodyNiedostepne()
        myLabelR.configure(text=f"Liczba niedostepnych samochodów: {liczba}")


        self.lista = Listbox(self.okno, selectmode=SINGLE, width=250, height=250)
        self.lista.pack()

    def wyswietlUzytkownikow(self):
        self.lista.delete(0, END)
        uzytkownicy = self.bazaUzytkownikow.wyswietlWszystkichUzytkownikow()
        if uzytkownicy:
            self.lista.insert(END, "ID | Nazwa | Hasło | Imię | Nazwisko | Liczba Wypożyczonych Samochodów | Pesel | Numer Telefonu")
            for uzytkownik in uzytkownicy:
                self.lista.insert(END, uzytkownik)
        else:
            print("Nie znaleziono uzytkownikow")

    def wyswietlSamochody(self):
        self.lista.delete(0, END)
        samochody = self.bazaSamochodow.wyswietlWszystkieSamochody()
        if samochody:
            self.lista.insert(END, "ID | Marka | Model | Rok Produkcji | Kolor | Dostępność")
            for samochod in samochody:
                self.lista.insert(END, samochod)
        else:
            print("Nie znaleziono samochodow")

    def wyswietlSamochodyDost(self):
        samochody = self.bazaSamochodow.wyswietlWszystkieSamochody()
        liczba = 0
        for samochod in samochody:
            if samochod[8] == "Dostępny":
                liczba += 1
        return liczba

    def wyswietlSamochodyZarezerwowane(self):
        samochody = self.bazaSamochodow.wyswietlWszystkieSamochody()
        liczba = 0
        for samochod in samochody:
            if samochod[8] == "Zarezerwowany":
                liczba += 1
        return liczba

    def wyswietlSamochodyWypozyczone(self):
        samochody = self.bazaSamochodow.wyswietlWszystkieSamochody()
        liczba = 0
        for samochod in samochody:
            if samochod[8] == "Wypożyczony":
                liczba += 1
        return liczba

    def wyswietlSamochodyNiedostepne(self):
        samochody = self.bazaSamochodow.wyswietlWszystkieSamochody()
        liczba = 0
        for samochod in samochody:
            if samochod[8] != "Dostępny":
                liczba += 1
        return liczba
    
    def wyswietlRezerwacje(self):
        self.lista.delete(0, END)
        samochody = self.bazaSamochodow.wyswietlanieRezerwacji()
        if samochody:
            self.lista.insert(END, "ID_klienta | ID_auta")
            for samochod in samochody:
                self.lista.insert(END, samochod)
        else:
            print("Nie znaleziono samochodow")

#WYpożyczanie

    def WypozyczSamochod(self):
        self.oknoWypozyczSamochodu = Toplevel(self.okno)
        self.oknoWypozyczSamochodu.geometry("500x500")
        self.oknoWypozyczSamochodu.configure(bg="#708090")

        myLabel = Label(self.oknoWypozyczSamochodu, text="Wypozycz Samochód", bg="#708090")
        myLabel.pack()

        self.odswiezDropdownMenuWypozycz()

        label_dropdown = Label(self.oknoWypozyczSamochodu, text="Wybierz samochód:")
        label_dropdown.pack()

        self.dropdown_samochody = ttk.Combobox(self.oknoWypozyczSamochodu, values=self.samochody_list)
        self.dropdown_samochody.pack()

        przycisk_usun = Button(self.oknoWypozyczSamochodu, text="Wypozycz samochód", command=self.WypozyczWybranySamochod)
        przycisk_usun.pack()


    def WypozyczWybranySamochod(self):
        wybrany_samochod = self.dropdown_samochody.get()
        id_samochodu = wybrany_samochod.split(" - ")[0]  # Pobierz ID samochodu z tekstu
        print("IDSAMOCHODU----",id_samochodu)

        cur = self.baza.conn.cursor()
        sql = "UPDATE Samochody SET dostepnosc = 'Wypozyczony' WHERE ID = %s"
        cur.execute(sql, (id_samochodu,))
        self.baza.conn.commit()
        cur.close()


        print("Samochód został Wypozyczony")
        self.oknoWypozyczSamochodu.withdraw()
        
    def odswiezDropdownMenuWypozycz(self):
        samochody = self.baza.wyswietlWszystkieSamochody()
        if samochody is not None:
            self.samochody_list = [
                f"{samochod[7]} - {samochod[0]} {samochod[2]}"
                for samochod in samochody
                if samochod[8] == "Zarezerwowany" 
            ]
            print(self.samochody_list)
        else:
            print("Błąd podczas pobierania danych.")

#Oddawanie
    def OddajSamochod(self):
        self.oknoOddajSamochodu = Toplevel(self.okno)
        self.oknoOddajSamochodu.geometry("500x500")
        self.oknoOddajSamochodu.configure(bg="#708090")

        myLabel = Label(self.oknoOddajSamochodu, text="Oddaj Samochód", bg="#708090")
        myLabel.pack()

        self.odswiezDropdownMenuOddaj()

        label_dropdown = Label(self.oknoOddajSamochodu, text="Wybierz samochód:")
        label_dropdown.pack()

        self.dropdown_samochody = ttk.Combobox(self.oknoOddajSamochodu, values=self.samochody_list)
        self.dropdown_samochody.pack()

        przycisk_usun = Button(self.oknoOddajSamochodu, text="Oddaj samochód", command=self.OddajWybranySamochod)
        przycisk_usun.pack()


    def OddajWybranySamochod(self):
        wybrany_samochod = self.dropdown_samochody.get()
        id_samochodu = wybrany_samochod.split(" - ")[0]  # Pobierz ID samochodu z tekstu
        print("IDSAMOCHODU----", id_samochodu)

        cur = self.baza.conn.cursor()
        sql = "UPDATE Samochody SET dostepnosc = 'Dostępny' WHERE ID = %s"
        cur.execute(sql, (id_samochodu,))
        self.baza.conn.commit()
        cur.close()


        print("Samochód został Oddany")
        self.oknoOddajSamochodu.withdraw()


    def odswiezDropdownMenuOddaj(self):
        samochody = self.baza.wyswietlWszystkieSamochody()
        if samochody is not None:
            self.samochody_list = [
            f"{samochod[7]} - {samochod[0]} {samochod[2]}"
            for samochod in samochody
            if samochod[8] == "Wypozyczony"
            ]
            print(self.samochody_list)
        else:
            print("Błąd podczas pobierania danych.")





if __name__ == "__main__":
    aplikacja = Pracownik()
    aplikacja.okno.mainloop()


from tkinter import *
import tkinter as tk

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





if __name__ == "__main__":
    aplikacja = Pracownik()
    aplikacja.okno.mainloop()

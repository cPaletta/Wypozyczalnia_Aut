from tkinter import *
from bazaUzytkownikow import bazaUzytkownikow
from bazaSamochodow import bazaSamochodow
import tkinter as tk
from Pracownik import Pracownik
from ZarzadzajSamochodami import ZarzadzajSamochodami
from ZarzadzajOsoba import ZarzadzajOsobami

class Admin(Pracownik):
    def __init__(self):
        self.specjalizacja = "Admin"

        self.okno = Tk()
        self.okno.configure(bg="#708090")
        self.okno.geometry("500x500")

        myLabel = Label(self.okno, text="Admin", bg="#708090")
        myLabel.pack()

        przyciskWyswietleniaUzytkownikow = Button(self.okno, text="Wyswietl uzytkownikow", command=self.wyswietlUzytkownikow)
        przyciskWyswietleniaUzytkownikow.pack()

        przyciskWyswietleniaSamochodow = Button(self.okno, text="Wyswietl samochody", command=self.wyswietlSamochody)
        przyciskWyswietleniaSamochodow.pack()

        self.bazaSamochodow = bazaSamochodow()
        self.bazaUzytkownikow = bazaUzytkownikow()
        self.ZarzadzajSamochodami = ZarzadzajSamochodami(self.okno)
        self.ZarzadzajOsoba = ZarzadzajOsobami(self.okno)

        przyciskDodaniaSamochodow = Button(self.okno, text="Dodaj samochod", command=self.ZarzadzajSamochodami.dodajSamochod)
        przyciskDodaniaSamochodow.pack()
        
        przyciskUsuwaniaSamochodow = Button(self.okno, text="Usun samochod", command=self.ZarzadzajSamochodami.usunSamochod)
        przyciskUsuwaniaSamochodow.pack()

        
        dodajOsobe = Button(self.okno, text="Dodaj osobe", command=self.ZarzadzajOsoba.dodajOsobe)
        dodajOsobe.pack()

        usunOsobe = Button(self.okno, text="Usun osobe", command=self.ZarzadzajOsoba.usunOsobe)
        usunOsobe.pack()

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

 

if __name__ == "__main__":
    aplikacja = Admin()
    aplikacja.okno.mainloop()

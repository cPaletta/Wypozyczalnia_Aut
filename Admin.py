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
        self.okno.configure(bg="#A5978B")
        self.okno.geometry("700x700")

        myLabel = Label(self.okno, text="Menu Admina", bg="#A5978B", font=("Georgia", 15))
        myLabel.pack()

        przyciskWyswietleniaUzytkownikow = Button(self.okno, text="Wyswietl uzytkownikow", command=self.wyswietlUzytkownikow,bg="#EEE7D4", font=("Georgia", 12))
        przyciskWyswietleniaUzytkownikow.pack()

        przyciskWyswietleniaSamochodow = Button(self.okno, text="Wyswietl samochody", command=self.wyswietlSamochody,bg="#EEE7D4", font=("Georgia", 12))
        przyciskWyswietleniaSamochodow.pack()

        self.bazaSamochodow = bazaSamochodow()
        self.bazaUzytkownikow = bazaUzytkownikow()
        self.ZarzadzajSamochodami = ZarzadzajSamochodami(self.okno)
        self.ZarzadzajOsoba = ZarzadzajOsobami(self.okno)
        self.baza=bazaSamochodow()

        przyciskDodaniaSamochodow = Button(self.okno, text="Dodaj samochod", command=self.ZarzadzajSamochodami.dodajSamochod,bg="#EEE7D4", font=("Georgia", 12))
        przyciskDodaniaSamochodow.pack()
        
        przyciskUsuwaniaSamochodow = Button(self.okno, text="Usun samochod", command=self.ZarzadzajSamochodami.usunSamochod,bg="#EEE7D4", font=("Georgia", 12))
        przyciskUsuwaniaSamochodow.pack()

        
        dodajOsobe = Button(self.okno, text="Dodaj osobe", command=self.ZarzadzajOsoba.dodajOsobe,bg="#EEE7D4", font=("Georgia", 12))
        dodajOsobe.pack()

        usunOsobe = Button(self.okno, text="Usun osobe", command=self.ZarzadzajOsoba.usunOsobe,bg="#EEE7D4", font=("Georgia", 12))
        usunOsobe.pack()

        przyciskWypozycz = Button(self.okno, text="Wypozycz", command=self.WypozyczSamochod,bg="#EEE7D4", font=("Georgia", 12))
        przyciskWypozycz.pack()

        przyciskOddaj = Button(self.okno, text="Oddaj", command=self.OddajSamochod,bg="#EEE7D4", font=("Georgia", 12))
        przyciskOddaj.pack()

        przyciskWyloguj = Button(self.okno, text="Wyloguj", command=self.wyloguj,bg="#EEE7D4", font=("Georgia", 12))
        przyciskWyloguj.pack()

        myLabell = Label(self.okno, text="Dostępne samochody:",bg="#A5978B", font=("Georgia", 12))
        myLabell.pack()

        liczba = self.wyswietlSamochodyDost()
        myLabell.configure(text=f"Liczba dostępnych samochodów: {liczba}",bg="#A5978B", font=("Georgia", 12))

        myLabelR = Label(self.okno, text="Zarezerwowane samochody:",bg="#A5978B", font=("Georgia", 12))
        myLabelR.pack()

        liczba = self.wyswietlSamochodyZarezerwowane()
        myLabelR.configure(text=f"Liczba zarezerwowanych samochodów: {liczba}",bg="#A5978B", font=("Georgia", 12))

        myLabelR = Label(self.okno, text="Niedostepne samochody:",bg="#A5978B", font=("Georgia", 12))
        myLabelR.pack()

        liczba = self.wyswietlSamochodyNiedostepne()
        myLabelR.configure(text=f"Liczba niedostepnych samochodów: {liczba}",bg="#A5978B", font=("Georgia", 12))


        self.lista = Listbox(self.okno, selectmode=SINGLE, width=103, height=15)
        self.lista.pack()

 

if __name__ == "__main__":
    aplikacja = Admin()
    aplikacja.okno.mainloop()

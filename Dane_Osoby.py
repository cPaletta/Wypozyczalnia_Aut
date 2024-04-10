from tkinter import *
from bazaUzytkownikow import bazaUzytkownikow
import tkinter as tk


class Dane_Osoby:
     

    def __init__(self,nazwaUzytkownika,idUzytkownika,hasloUzytkownika,imie,nazwisko,liczba_wypozyczonych_samochodow,pesel,numer_telefonu):
        
        self.nazwaUzytkownika = nazwaUzytkownika
        self.hasloUzytkownika = hasloUzytkownika
        self.Imie = imie
        self.Nazwisko = nazwisko
        self.LiczbaWypozyczonychSamochodow = liczba_wypozyczonych_samochodow
        self.Pesel = pesel
        self.Numer_Telefonu = numer_telefonu
        self.idUzytkownika = idUzytkownika


   #chyba nei ma co robic tego jak juz zrobilem to w kliencie



if __name__ == "__main__":
    aplikacja = Dane_Osoby(
    nazwaUzytkownika="jan",
    idUzytkownika=5,
    hasloUzytkownika="kowalski",
    imie="Imie",
    nazwisko="Nazwisko",
    liczba_wypozyczonych_samochodow=3,
    pesel="12345678901",
    numer_telefonu="123-456-789")

    aplikacja.okno.mainloop()
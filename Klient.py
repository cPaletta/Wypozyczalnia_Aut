from tkinter import *
from bazaUzytkownikow import bazaUzytkownikow
import tkinter as tk

class Klient:
    def __init__(self,nazwaUzytkownika,idUzytkownika,hasloUzytkownika,imie,nazwisko,liczba_wypozyczonych_samochodow,pesel,numer_telefonu):
        
        self.nazwaUzytkownika = nazwaUzytkownika
        self.hasloUzytkownika = hasloUzytkownika
        self.Imie = imie
        self.Nazwisko = nazwisko
        self.LiczbaWypozyczonychSamochodow = liczba_wypozyczonych_samochodow
        self.Pesel = pesel
        self.Numer_Telefonu = numer_telefonu
        self.idUzytkownika = idUzytkownika
        
        self.okno = Tk()
        self.okno.configure(bg="#708090")
        self.okno.geometry("500x500")
        
        myLabel = Label(self.okno, text="klient!", bg="#708090")
        myLabel.pack()

        myLabel = Label(self.okno, text="Witaj w wypożyczalni aut!", bg="#708090")
        myLabel.pack()

        przyciskZmianyDanych = Button(self.okno, text="Zmiana Danych", command=self.aktulizujProfil)
        przyciskZmianyDanych.pack()

        przyciskWyloguj = Button(self.okno, text="Wyloguj", command=self.wyloguj)
        przyciskWyloguj.pack()

    def pokazDane(self):
        print(f"Nazwa użytkownika: {self.nazwaUzytkownika}")
        print(f"Hasło użytkownika: {self.hasloUzytkownika}")
        print(f"Imię: {self.Imie}")
        print(f"Nazwisko: {self.Nazwisko}")
        print(f"Liczba wypożyczonych samochodów: {self.LiczbaWypozyczonychSamochodow}")
        print(f"Pesel: {self.Pesel}")
        print(f"Numer telefonu: {self.Numer_Telefonu}")
        print(f"ID użytkownika: {self.idUzytkownika}")
    
    def aktulizujProfil(self):
        self.oknoZmianDanych = Toplevel(self.okno)
        self.oknoZmianDanych.geometry("500x500")
        self.oknoZmianDanych.configure(bg="#708090")

        myLabel = Label(self.oknoZmianDanych, text="Zmien swoje dane", bg="#708090")
        myLabel.pack()

        # Etykieta i pole dla nazwy użytkownika
        label_nazwa_uzytkownika = Label(self.oknoZmianDanych, text="Nazwa użytkownika:")
        label_nazwa_uzytkownika.pack()
        self.wejscieNazwy = Entry(self.oknoZmianDanych)
        self.wejscieNazwy.insert(0, self.nazwaUzytkownika) 
        self.wejscieNazwy.pack()

        # Etykieta i pole dla hasła
        label_haslo = Label(self.oknoZmianDanych, text="Hasło:")
        label_haslo.pack()
        self.wejscieHasla = Entry(self.oknoZmianDanych, show="*")
        self.wejscieHasla.insert(0, self.hasloUzytkownika) 
        self.wejscieHasla.pack()

        # Etykieta i pole dla imienia
        label_imie = Label(self.oknoZmianDanych, text="Imię:")
        label_imie.pack()
        self.wejscieImie = Entry(self.oknoZmianDanych)
        self.wejscieImie.insert(0, self.Imie)
        self.wejscieImie.pack()

        # Etykieta i pole dla nazwiska
        label_nazwisko = Label(self.oknoZmianDanych, text="Nazwisko:")
        label_nazwisko.pack()
        self.wejscieNazwisko = Entry(self.oknoZmianDanych)
        self.wejscieNazwisko.insert(0, self.Nazwisko)
        self.wejscieNazwisko.pack()

        # Etykieta i pole dla PESEL
        label_pesel = Label(self.oknoZmianDanych, text="PESEL:")
        label_pesel.pack()
        self.wejsciePesel = Entry(self.oknoZmianDanych)
        self.wejsciePesel.insert(0, self.Pesel)
        self.wejsciePesel.pack()

        # Etykieta i pole dla numeru telefonu
        label_numer_telefonu = Label(self.oknoZmianDanych, text="Numer telefonu:")
        label_numer_telefonu.pack()
        self.wejscieNumerTelefonu = Entry(self.oknoZmianDanych)
        self.wejscieNumerTelefonu.insert(0, self.Numer_Telefonu)
        self.wejscieNumerTelefonu.pack()

        
        

        przyciskZmianyDanych = Button(self.oknoZmianDanych, text="Zmiana danych", command=self.zapiszZmiany)
        przyciskZmianyDanych.pack()




    def wyloguj(self):
         
        from Menadzer_Logowania import Logowanie
        oknoLogowania = Logowanie()
        self.okno.destroy()

       

    def zapiszZmiany(self):
        
        uzytkownik = self.wejscieNazwy.get()
        haslo = self.wejscieHasla.get()
        imie = self.wejscieImie.get()
        nazwisko = self.wejscieNazwisko.get()
        pesel = self.wejsciePesel.get()
        numer_telefonu = self.wejscieNumerTelefonu.get()
        
        baza = bazaUzytkownikow()
        baza.zmianaDanych(uzytkownik,haslo,imie,nazwisko,pesel,numer_telefonu,self.idUzytkownika)
        self.oknoZmianDanych.withdraw()
        
        self.nazwaUzytkownika = uzytkownik
        self.hasloUzytkownika = haslo
        self.Imie = imie
        self.Nazwisko = nazwisko
        self.Pesel = pesel
        self.Numer_Telefonu = numer_telefonu
        
        

if __name__ == "__main__":
    aplikacja = Klient(
    nazwaUzytkownika="jan",
    idUzytkownika=5,
    hasloUzytkownika="kowalski",
    imie="Imie",
    nazwisko="Nazwisko",
    liczba_wypozyczonych_samochodow=3,
    pesel="12345678901",
    numer_telefonu="123-456-789")

    aplikacja.okno.mainloop()





    

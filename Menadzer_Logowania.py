from tkinter import *
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

from Menadzer_Rejestracji import Rejestracja
from bazaUzytkownikow import bazaUzytkownikow
from Klient import Klient
from Pracownik import Pracownik
from Admin import Admin


class Logowanie:
    def __init__(self):
        self.okno = Tk()
        self.okno.configure(bg="#708090", height=431, width=626)
        self.okno.geometry("500x500")

        myLabel = Label(self.okno, text="Witaj w wypożyczalni aut!", bg="#708090")
        myLabel.pack()

        self.wejscieNazwy = Entry(self.okno)
        self.wejscieNazwy.pack()

        self.wejscieHasla = Entry(self.okno, show="*")
        self.wejscieHasla.pack()

        przyciskLogowania = Button(self.okno, text="Login", command=self.otrzymajDane)
        przyciskLogowania.pack()

        przyciskRejestracji = Button(self.okno, text="Register", command=self.otworzRejestracje)
        przyciskRejestracji.pack()

    def otrzymajDane(self):
        nazwaUzytkownika = self.wejscieNazwy.get()
        hasloUzytkownika = self.wejscieHasla.get()
        print(nazwaUzytkownika, hasloUzytkownika)


        baza = bazaUzytkownikow()
        if (nazwaUzytkownika == "admin" and hasloUzytkownika == "admin"):
            self.otworzAdmina()
            self.okno.withdraw()
        elif (nazwaUzytkownika == "pracownik" and hasloUzytkownika == "pracownik"):  
            self.otworzPracownika()
            self.okno.withdraw()
        else: walidacja = baza.Walidacja(nazwaUzytkownika,hasloUzytkownika)        
        
        if walidacja and len(walidacja[0]) > 0:
            idUzytkownika = walidacja[0][0]
        
            imieUzytkownika = walidacja[0][3]
            nazwiskoUzytkownika = walidacja[0][4]
            liczba_wypozyczonych_samochodowUzytkownika = walidacja[0][5]
            peselUzytkownika = walidacja[0][6]
            numerTelefonuUzytkownika = walidacja[0][7]
            print(nazwaUzytkownika,hasloUzytkownika,idUzytkownika,imieUzytkownika,nazwiskoUzytkownika,liczba_wypozyczonych_samochodowUzytkownika,peselUzytkownika,numerTelefonuUzytkownika)
        else:
            print("Użytkownik nie istnieje w bazie danych.")

        if walidacja:
            tk.messagebox.showinfo("Logowanie udane", "Witaj {}".format(nazwaUzytkownika))
            self.otworzKlienta(nazwaUzytkownika,hasloUzytkownika,idUzytkownika,imieUzytkownika,nazwiskoUzytkownika,liczba_wypozyczonych_samochodowUzytkownika,peselUzytkownika,numerTelefonuUzytkownika)
            self.okno.withdraw()
        else:
            tk.messagebox.showerror("Logowanie nieudane", "Niepoprawne dane")




    def otworzRejestracje(self):
        oknoRejestracji = Rejestracja()
    
    def otworzKlienta(self, nazwaUzytkownika, hasloUzytkownika, idUzytkownika, imieUzytkownika, nazwiskoUzytkownika, liczba_wypozyczonych_samochodowUzytkownika, peselUzytkownika, numerTelefonuUzytkownika):
        oknoKlienta = Klient(nazwaUzytkownika, idUzytkownika, hasloUzytkownika, imieUzytkownika, nazwiskoUzytkownika, liczba_wypozyczonych_samochodowUzytkownika, peselUzytkownika, numerTelefonuUzytkownika)

    def otworzAdmina(self):
        oknoAdmina = Admin()
    def otworzPracownika(self):
        oknoPracownika = Pracownik()

if __name__ == "__main__":
    aplikacja = Logowanie()
    aplikacja.okno.mainloop()

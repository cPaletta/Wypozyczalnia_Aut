from tkinter import *
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from tkinter import font

from Menadzer_Rejestracji import Rejestracja
from bazaUzytkownikow import bazaUzytkownikow
from Klient import Klient
from Pracownik import Pracownik
from Admin import Admin


class Logowanie:
    def __init__(self):
        self.okno = Tk()
        self.okno.configure(bg="#5C4742", height=400, width=800)
        self.okno.geometry("670x470")

        czcionka1 = font.Font(family="Georgia", size=20, weight="normal", slant="roman")
        czcionka2 = font.Font(family="Georgia", size=12)
        czcionka3 = font.Font(family="Georgia", size=16)

        bezowyPasek = Frame(self.okno, bg="#A5978B", width=370)  
        bezowyPasek.pack(side="left", fill="y") 

        myLabel = Label(self.okno, text="Witaj w wypożyczalni \n samochodów!", bg="#A5978B", font=czcionka1)
        myLabel.pack()
        myLabel.place(x=40,y=30)

        myLabel2 = Label(self.okno, text = "Zaloguj się na swoje konto", bg="#5C4742", font=czcionka3)
        myLabel2.pack()
        myLabel2.place(x=400,y=55)

        self.wejscieNazwy = Entry(self.okno, font=("Arial", 12), width=20, borderwidth=3, highlightcolor="black")
        self.wejscieNazwy.pack()
        self.wejscieNazwy.place(x=440, y=120)
       
        myLabel5= Label(self.okno, text = "Login:", bg="#5C4742", font=czcionka2)
        myLabel5.pack()
        myLabel5.place(x=390,y=120)

        self.wejscieHasla = Entry(self.okno, show="*", font=("Arial", 12), width=20, borderwidth=3, highlightcolor="black")
        self.wejscieHasla.pack()
        self.wejscieHasla.place(x=440, y=160)

        myLabel4 = Label(self.okno, text = "Hasło:", bg="#5C4742", font=czcionka2)
        myLabel4.pack()
        myLabel4.place(x=390,y=160)

        przyciskLogowania = Button(self.okno, text="Zaloguj się", command=self.otrzymajDane, font=("Georgia", 11), bg="#FFF5EE", fg="black", height=1, borderwidth=2, relief="sunken")
        przyciskLogowania.pack()
        przyciskLogowania.place(x=490, y=200)

        myLabel3 = Label(self.okno, text="Nie masz konta?\n Klinkij przycisk zarejestruj", bg="#5C4742", font=czcionka2)
        myLabel3.pack()
        myLabel3.place(x=420,y=270)

        przyciskRejestracji = Button(self.okno, text="Zarejestruj", command=self.otworzRejestracje, font=("Georgia", 11), bg="#FFF5EE", fg="black", height=1, borderwidth=2, relief="sunken")
        przyciskRejestracji.pack()
        przyciskRejestracji.place(x=490, y=320)

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

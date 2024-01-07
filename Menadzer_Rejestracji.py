from tkinter import *
from bazaUzytkownikow import bazaUzytkownikow
import tkinter as tk

class Rejestracja:
    
    def __init__(self):
        self.okno = Tk()
        self.okno.configure(bg="#708090")
        self.okno.geometry("500x500")

        myLabel = Label(self.okno, text="Witaj w wypożyczalni aut!", bg="#708090")
        myLabel.pack()

        # Etykieta i pole dla nazwy użytkownika
        label_nazwa_uzytkownika = Label(self.okno, text="Nazwa użytkownika:")
        label_nazwa_uzytkownika.pack()
        self.wejscieNazwy = Entry(self.okno)
        self.wejscieNazwy.pack()

        # Etykieta i pole dla hasła
        label_haslo = Label(self.okno, text="Hasło:")
        label_haslo.pack()
        self.wejscieHasla = Entry(self.okno, show="*")
        self.wejscieHasla.pack()

        # Etykieta i pole dla imienia
        label_imie = Label(self.okno, text="Imię:")
        label_imie.pack()
        self.wejscieImie = Entry(self.okno)
        self.wejscieImie.pack()

        # Etykieta i pole dla nazwiska
        label_nazwisko = Label(self.okno, text="Nazwisko:")
        label_nazwisko.pack()
        self.wejscieNazwisko = Entry(self.okno)
        self.wejscieNazwisko.pack()


        # Etykieta i pole dla PESEL
        label_pesel = Label(self.okno, text="PESEL:")
        label_pesel.pack()
        self.wejsciePesel = Entry(self.okno)
        self.wejsciePesel.pack()

        # Etykieta i pole dla numeru telefonu
        label_numer_telefonu = Label(self.okno, text="Numer telefonu:")
        label_numer_telefonu.pack()
        self.wejscieNumerTelefonu = Entry(self.okno)
        self.wejscieNumerTelefonu.pack() 
        
        przyciskTworzeniaKonta = Button(self.okno, text="Stworz Konto", command=self.tworzenieKonta)
        przyciskTworzeniaKonta.pack()



    def tworzenieKonta(self):
        uzytkownik = self.wejscieNazwy.get()
        haslo = self.wejscieHasla.get()
        imie = self.wejscieImie.get()
        nazwisko = self.wejscieNazwisko.get()
        liczba_wypozyczonych_samochodow = 0
        pesel = self.wejsciePesel.get()
        numer_telefonu = self.wejscieNumerTelefonu.get()

        baza = bazaUzytkownikow()
        dodanie = baza.dodajUzytkownika(uzytkownik, haslo, imie, nazwisko, liczba_wypozyczonych_samochodow, pesel, numer_telefonu)
        if dodanie:
            tk.messagebox.showinfo("Utworzono konto", "Udalo sie utworzyc konto")
            self.okno.withdraw()
        else:
            tk.messagebox.showerror("Informacja", "Nie udalo sie dodac konta")

        

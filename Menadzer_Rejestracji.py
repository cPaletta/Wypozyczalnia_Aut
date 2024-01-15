from tkinter import *
from bazaUzytkownikow import bazaUzytkownikow
import tkinter as tk

class Rejestracja:
    
    def __init__(self):
        self.okno = Tk()
        self.okno.configure(bg="#A5978B")
        self.okno.geometry("500x500")

        myLabel = Label(self.okno, text="Aby stworzyć konto podaj \n następujące dane:", bg="#A5978B", font=("Georgia", 20))
        myLabel.pack()

        # Etykieta i pole dla nazwy użytkownika
        label_nazwa_uzytkownika = Label(self.okno, text="Nazwa użytkownika:",bg="#A5978B", font=("Georgia", 12))
        label_nazwa_uzytkownika.pack()
        self.wejscieNazwy = Entry(self.okno,bg="#A5978B", font=("Georgia", 12))
        self.wejscieNazwy.pack()

        # Etykieta i pole dla hasła
        label_haslo = Label(self.okno, text="Hasło:",bg="#A5978B", font=("Georgia", 12))
        label_haslo.pack()
        self.wejscieHasla = Entry(self.okno, show="*",bg="#A5978B", font=("Georgia", 12))
        self.wejscieHasla.pack()

        # Etykieta i pole dla imienia
        label_imie = Label(self.okno, text="Imię:",bg="#A5978B", font=("Georgia", 12))
        label_imie.pack()
        self.wejscieImie = Entry(self.okno,bg="#A5978B", font=("Georgia", 12))
        self.wejscieImie.pack()

        # Etykieta i pole dla nazwiska
        label_nazwisko = Label(self.okno, text="Nazwisko:",bg="#A5978B", font=("Georgia", 12))
        label_nazwisko.pack()
        self.wejscieNazwisko = Entry(self.okno,bg="#A5978B", font=("Georgia", 12))
        self.wejscieNazwisko.pack()


        # Etykieta i pole dla PESEL
        label_pesel = Label(self.okno, text="PESEL:",bg="#A5978B", font=("Georgia", 12))
        label_pesel.pack()
        self.wejsciePesel = Entry(self.okno,bg="#A5978B", font=("Georgia", 12))
        self.wejsciePesel.pack()

        # Etykieta i pole dla numeru telefonu
        label_numer_telefonu = Label(self.okno, text="Numer telefonu:",bg="#A5978B", font=("Georgia", 12))
        label_numer_telefonu.pack()
        self.wejscieNumerTelefonu = Entry(self.okno,bg="#A5978B", font=("Georgia", 12))
        self.wejscieNumerTelefonu.pack() 
        
        przyciskTworzeniaKonta = Button(self.okno, text="Stworz Konto", command=self.tworzenieKonta,bg="#A5978B", font=("Georgia", 12))
        przyciskTworzeniaKonta.pack()
        przyciskTworzeniaKonta.place(x=190,y=360)



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

        

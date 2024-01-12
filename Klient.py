from tkinter import *
from bazaUzytkownikow import bazaUzytkownikow
from bazaSamochodow import bazaSamochodow
from ZarzadzajSamochodami import ZarzadzajSamochodami
import tkinter as tk
import tkinter.ttk as ttk


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
        self.baza=bazaSamochodow()
        
        self.okno = Tk()
        self.okno.configure(bg="#708090")
        self.okno.geometry("500x500")
        
        myLabel = Label(self.okno, text="klient!", bg="#708090")
        myLabel.pack()

        myLabel = Label(self.okno, text="Witaj w wypożyczalni aut!", bg="#708090")
        myLabel.pack()

        przyciskZmianyDanych = Button(self.okno, text="Zmiana Danych", command=self.aktulizujProfil)
        przyciskZmianyDanych.pack()

        self.bazaSamochodow = bazaSamochodow()
        self.ZarzadzajSamochodami = ZarzadzajSamochodami(self.okno)

        przyciskRezerwacji = Button(self.okno, text="Rezerwuj Samochód", command=self.rezerwujSamochod )
        przyciskRezerwacji.pack()

        przyciskWyloguj = Button(self.okno, text="Wyloguj", command=self.wyloguj)
        przyciskWyloguj.pack()


    def rezerwujSamochod(self):
        self.oknoRezerwacjiSamochodu = Toplevel(self.okno)
        self.oknoRezerwacjiSamochodu.geometry("500x500")
        self.oknoRezerwacjiSamochodu.configure(bg="#708090")

        myLabel = Label(self.oknoRezerwacjiSamochodu, text="Rezerwuj Samochód", bg="#708090")
        myLabel.pack()

        self.odswiezDropdownMenuRezerwacja()

        label_dropdown = Label(self.oknoRezerwacjiSamochodu, text="Wybierz samochód:")
        label_dropdown.pack()

        self.dropdown_samochody = ttk.Combobox(self.oknoRezerwacjiSamochodu, values=self.samochody_list)
        self.dropdown_samochody.pack()

        przycisk_usun = Button(self.oknoRezerwacjiSamochodu, text="Rezerwuj samochód", command=self.rezerwujWybranySamochod)
        przycisk_usun.pack()


    def rezerwujWybranySamochod(self):
        wybrany_samochod = self.dropdown_samochody.get()
        id_samochodu = wybrany_samochod.split(" - ")[0]  # Pobierz ID samochodu z tekstu
        print("IDSAMOCHODU----",id_samochodu)

        cur = self.baza.conn.cursor()
        sql = "UPDATE Samochody SET dostepnosc = 'Zarezerwowany' WHERE ID = %s"
        cur.execute(sql, (id_samochodu,))
        self.baza.conn.commit()
        cur.close()

        id_klienta=self.idUzytkownika

        cur = self.baza.conn.cursor()
        sql = "INSERT INTO rezerwacje (id_klienta, id_samochodu) VALUES (%s, %s)"
        cur.execute(sql, (id_klienta, id_samochodu))
        self.baza.conn.commit()
        cur.close()

        print("Samochód został zarezerwowany")
        self.oknoRezerwacjiSamochodu.withdraw()
        
    def odswiezDropdownMenuRezerwacja(self):
        samochody = self.baza.wyswietlWszystkieSamochody()
        if samochody is not None:
            self.samochody_list = [
                f"{samochod[7]} - {samochod[0]} {samochod[2]}"
                for samochod in samochody
                if samochod[8] == "Dostępny" 
            ]
            print(self.samochody_list)
        else:
            print("Błąd podczas pobierania danych.")


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


    # def rezerwacjaDB(self):
        
    #     id_klienta=self.Klient.idUzytkownika
    #     id_samochodu=self.Samochod.ID

    #     cur = self.baza.conn.cursor()
    #     sql = "INSERT INTO rezerwacje (id_klienta, id_samochodu) VALUES (%s, %s)"
    #     cur.execute(sql, (id_klienta, id_samochodu))
    #     self.baza.conn.commit()
    #     cur.close()


       

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





    

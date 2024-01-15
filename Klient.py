from tkinter import *
from bazaUzytkownikow import bazaUzytkownikow
from bazaSamochodow import bazaSamochodow
from ZarzadzajSamochodami import ZarzadzajSamochodami
import tkinter as tk 
import tkinter as font
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
        self.okno.configure(bg="#A5978B")
        self.okno.geometry("500x400")
        
        myLabel = Label(self.okno, text="Witaj ponownie {}!".format(nazwaUzytkownika), bg="#A5978B" , font=("Georgia", 20))
        myLabel.pack()
        myLabel.place(x=125, y=20)

        myLabel = Label(self.okno, text="Wybierz jedna z opcji:", bg="#A5978B", font=("Georgia", 12))
        myLabel.pack()   
        myLabel.place(x=85, y=90)

        przyciskZmianyDanych = Button(self.okno, text="Zaktualizuj Dane", command=self.aktulizujProfil,font=("Georgia", 11), bg="#FFF5EE", fg="black", height=1, borderwidth=2, relief="sunken")
        przyciskZmianyDanych.pack()
        przyciskZmianyDanych.place(x=125, y=140)

        self.bazaSamochodow = bazaSamochodow()
        self.ZarzadzajSamochodami = ZarzadzajSamochodami(self.okno)

        przyciskRezerwacji = Button(self.okno, text="Zarezerwuj Samochód", command=self.rezerwujSamochod, font=("Georgia", 11), bg="#FFF5EE", fg="black", height=1, borderwidth=2, relief="sunken")
        przyciskRezerwacji.pack()
        przyciskRezerwacji.place(x=125, y=200)

        przyciskWyloguj = Button(self.okno, text="Wyloguj", command=self.wyloguj,font=("Georgia", 11), bg="#FFF5EE", fg="black", height=1, borderwidth=2, relief="sunken")
        przyciskWyloguj.pack()
        przyciskWyloguj.place(x=125, y=260)


    def rezerwujSamochod(self):
        self.oknoRezerwacjiSamochodu = Toplevel(self.okno)
        self.oknoRezerwacjiSamochodu.geometry("500x200")
        self.oknoRezerwacjiSamochodu.configure(bg="#A5978B")

        myLabel = Label(self.oknoRezerwacjiSamochodu, text="Rezerwuj Samochód", bg="#A5978B", font=("Georgia", 15))
        myLabel.pack()

        self.odswiezDropdownMenuRezerwacja()

        label_dropdown = Label(self.oknoRezerwacjiSamochodu, text="Wybierz samochód:", bg="#A5978B", font=("Georgia", 12))
        label_dropdown.pack()

        self.dropdown_samochody = ttk.Combobox(self.oknoRezerwacjiSamochodu, values=self.samochody_list)
        self.dropdown_samochody.pack()

        przycisk_usun = Button(self.oknoRezerwacjiSamochodu, text="Rezerwuj samochód", command=self.rezerwujWybranySamochod, bg="white", font=("Georgia", 12))
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
        self.oknoZmianDanych.geometry("500x400")
        self.oknoZmianDanych.configure(bg="#A5978B")

        myLabel = Label(self.oknoZmianDanych, text="Zmien swoje dane", bg="#A5978B",font=("Georgia", 15))
        myLabel.pack()

        # Etykieta i pole dla nazwy użytkownika
        label_nazwa_uzytkownika = Label(self.oknoZmianDanych, text="Nazwa użytkownika:", bg="#A5978B", font=("Georgia", 12))
        label_nazwa_uzytkownika.pack()
        self.wejscieNazwy = Entry(self.oknoZmianDanych, bg="#A5978B", font=("Georgia", 12))
        self.wejscieNazwy.insert(0, self.nazwaUzytkownika) 
        self.wejscieNazwy.pack()

        # Etykieta i pole dla hasła
        label_haslo = Label(self.oknoZmianDanych, text="Hasło:", bg="#A5978B", font=("Georgia", 12))
        label_haslo.pack()
        self.wejscieHasla = Entry(self.oknoZmianDanych, show="*", bg="#A5978B", font=("Georgia", 12))
        self.wejscieHasla.insert(0, self.hasloUzytkownika) 
        self.wejscieHasla.pack()

        # Etykieta i pole dla imienia
        label_imie = Label(self.oknoZmianDanych, text="Imię:", bg="#A5978B", font=("Georgia", 12))
        label_imie.pack()
        self.wejscieImie = Entry(self.oknoZmianDanych, bg="#A5978B", font=("Georgia", 12))
        self.wejscieImie.insert(0, self.Imie)
        self.wejscieImie.pack()

        # Etykieta i pole dla nazwiska
        label_nazwisko = Label(self.oknoZmianDanych, text="Nazwisko:", bg="#A5978B", font=("Georgia", 12))
        label_nazwisko.pack()
        self.wejscieNazwisko = Entry(self.oknoZmianDanych, bg="#A5978B", font=("Georgia", 12))
        self.wejscieNazwisko.insert(0, self.Nazwisko)
        self.wejscieNazwisko.pack()

        # Etykieta i pole dla PESEL
        label_pesel = Label(self.oknoZmianDanych, text="PESEL:", bg="#A5978B", font=("Georgia", 12))
        label_pesel.pack()
        self.wejsciePesel = Entry(self.oknoZmianDanych, bg="#A5978B", font=("Georgia", 12))
        self.wejsciePesel.insert(0, self.Pesel)
        self.wejsciePesel.pack()

        # Etykieta i pole dla numeru telefonu
        label_numer_telefonu = Label(self.oknoZmianDanych, text="Numer telefonu:", bg="#A5978B", font=("Georgia", 12))
        label_numer_telefonu.pack()
        self.wejscieNumerTelefonu = Entry(self.oknoZmianDanych, bg="#A5978B", font=("Georgia", 12))
        self.wejscieNumerTelefonu.insert(0, self.Numer_Telefonu)
        self.wejscieNumerTelefonu.pack()

        
        

        przyciskZmianyDanych = Button(self.oknoZmianDanych, text="Zmiana danych", command=self.zapiszZmiany, bg="#A5978B", font=("Georgia", 12))
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





    

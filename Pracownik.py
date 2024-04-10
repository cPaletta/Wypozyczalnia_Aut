
from tkinter import *
import tkinter as tk
import tkinter.ttk as ttk

from Klient import Klient
from bazaSamochodow import bazaSamochodow
from bazaUzytkownikow import bazaUzytkownikow
from ZarzadzajSamochodami import ZarzadzajSamochodami

class Pracownik(Klient):
    
    def __init__(self):
        self.stanowsiko = "Pracownik"

        self.okno = Tk()
        self.okno.configure(bg="#5C4742")
        self.okno.geometry("650x800")
        self.baza=bazaSamochodow()

        myLabel = Label(self.okno, text="Menu", bg="#5C4742", font=("Georgia", 20))
        myLabel.pack()
        myLabel.place(x=250,y=10)
      

        self.bazaUzytkownikow = bazaUzytkownikow()
        self.ZarzadzajSamochodami = ZarzadzajSamochodami(self.okno)
        self.bazaSamochodow = bazaSamochodow()

        przyciskWyswietleniaUzytkownikow = Button(self.okno, text="Wyswietl uzytkownikow", command=self.wyswietlUzytkownikow,font=("Georgia", 11), bg="#FFF5EE", fg="black", height=1, borderwidth=2, relief="sunken")
        przyciskWyswietleniaUzytkownikow.pack()
        przyciskWyswietleniaUzytkownikow.place(x=180,y=50)

        przyciskWyswietleniaSamochodow = Button(self.okno, text="Wyswietl samochody", command=self.wyswietlSamochody,font=("Georgia", 11), bg="#FFF5EE", fg="black", height=1, borderwidth=2, relief="sunken")
        przyciskWyswietleniaSamochodow.pack()
        przyciskWyswietleniaSamochodow.place(x=180, y=90)
        

        przyciskDodaniaSamochodow = Button(self.okno, text="Dodaj samochod", command=self.ZarzadzajSamochodami.dodajSamochod,font=("Georgia", 11), bg="#FFF5EE", fg="black", height=1, borderwidth=2, relief="sunken")
        przyciskDodaniaSamochodow.pack()
        przyciskDodaniaSamochodow.place(x=180, y=130)
       

        przyciskUsuwaniaSamochodow = Button(self.okno, text="Usun samochod", command=self.ZarzadzajSamochodami.usunSamochod,font=("Georgia", 11), bg="#FFF5EE", fg="black", height=1, borderwidth=2, relief="sunken")
        przyciskUsuwaniaSamochodow.pack()
        przyciskUsuwaniaSamochodow.place(x=180,y=170)
        

        przyciskWyswietlRezerwacje = Button(self.okno, text="Wyświetl rezerwacje", command=self.wyswietlRezerwacje,font=("Georgia", 11), bg="#FFF5EE", fg="black", height=1, borderwidth=2, relief="sunken")
        przyciskWyswietlRezerwacje.pack()
        przyciskWyswietlRezerwacje.place(x=180, y=210)
        

        przyciskWypozycz = Button(self.okno, text="Wypozycz", command=self.WypozyczSamochod,font=("Georgia", 11), bg="#FFF5EE", fg="black", height=1, borderwidth=2, relief="sunken")
        przyciskWypozycz.pack()
        przyciskWypozycz.place(x=180,y=250)
       

        przyciskOddaj = Button(self.okno, text="Oddaj", command=self.OddajSamochod,font=("Georgia", 11), bg="#FFF5EE", fg="black", height=1, borderwidth=2, relief="sunken")
        przyciskOddaj.pack()
        przyciskOddaj.place(x=180,y=290)

        przyciskWyloguj = Button(self.okno, text="Wyloguj", command=self.wyloguj,font=("Georgia", 11), bg="#FFF5EE", fg="black", height=1, borderwidth=2, relief="sunken")
        przyciskWyloguj.pack()
        przyciskWyloguj.place(x=180,y=330)

        myLabell = Label(self.okno, text="Dostępne samochody:", bg="#B3A087")
        myLabell.pack()
        myLabell.place(x=180,y=370)

        liczba = self.wyswietlSamochodyDost()
        myLabell.configure(text=f"Liczba dostępnych samochodów: {liczba}", font=("Georgia", 14), bg="#B3A087")
        myLabell.place(x=15,y=410)

        myLabelR = Label(self.okno, text="Zarezerwowane samochody:", font=("Georgia", 14), bg="#B3A087")
        myLabelR.pack()
        myLabelR.place(x=15,y=450)

        liczba = self.wyswietlSamochodyZarezerwowane()
        myLabelR.configure(text=f"Liczba zarezerwowanych samochodów: {liczba}", font=("Georgia", 14), bg="#B3A087")

        myLabelR = Label(self.okno, text="Niedostepne samochody:",font=("Georgia", 14), bg="#B3A087")
        myLabelR.pack()
        myLabelR.place(x=15,y=490)

        liczba = self.wyswietlSamochodyNiedostepne()
        myLabelR.configure(text=f"Liczba niedostepnych samochodów: {liczba}")
        myLabelR.place(x=15,y=490)

        self.lista = Listbox(self.okno, selectmode=SINGLE, width=103, height=15)
        self.lista.pack()
        self.lista.place(x=15, y=525)

    def wyswietlUzytkownikow(self):
        self.lista.delete(0, END)
        uzytkownicy = self.bazaUzytkownikow.wyswietlWszystkichUzytkownikow()
        if uzytkownicy:
            self.lista.insert(END, "ID | Nazwa | Hasło | Imię | Nazwisko | Liczba Wypożyczonych Samochodów | Pesel | Numer Telefonu")
            for uzytkownik in uzytkownicy:
                self.lista.insert(END, uzytkownik)
        else:
            print("Nie znaleziono uzytkownikow")

    def wyswietlSamochody(self):
        self.lista.delete(0, END)
        samochody = self.bazaSamochodow.wyswietlWszystkieSamochody()
        if samochody:
            self.lista.insert(END, "ID | Marka | Model | Rok Produkcji | Kolor | Dostępność")
            for samochod in samochody:
                self.lista.insert(END, samochod)
        else:
            print("Nie znaleziono samochodow")

    def wyswietlSamochodyDost(self):
        samochody = self.bazaSamochodow.wyswietlWszystkieSamochody()
        liczba = 0
        for samochod in samochody:
            if samochod[8] == "Dostępny":
                liczba += 1
        return liczba

    def wyswietlSamochodyZarezerwowane(self):
        samochody = self.bazaSamochodow.wyswietlWszystkieSamochody()
        liczba = 0
        for samochod in samochody:
            if samochod[8] == "Zarezerwowany":
                liczba += 1
        return liczba

    def wyswietlSamochodyWypozyczone(self):
        samochody = self.bazaSamochodow.wyswietlWszystkieSamochody()
        liczba = 0
        for samochod in samochody:
            if samochod[8] == "Wypożyczony":
                liczba += 1
        return liczba

    def wyswietlSamochodyNiedostepne(self):
        samochody = self.bazaSamochodow.wyswietlWszystkieSamochody()
        liczba = 0
        for samochod in samochody:
            if samochod[8] != "Dostępny":
                liczba += 1
        return liczba
    
    def wyswietlRezerwacje(self):
        self.lista.delete(0, END)
        samochody = self.bazaSamochodow.wyswietlanieRezerwacji()
        if samochody:
            self.lista.insert(END, "ID_klienta | ID_auta")
            for samochod in samochody:
                self.lista.insert(END, samochod)
        else:
            print("Nie znaleziono samochodow")

#WYpożyczanie

    def WypozyczSamochod(self):
        self.oknoWypozyczSamochodu = Toplevel(self.okno)
        self.oknoWypozyczSamochodu.geometry("400x200")
        self.oknoWypozyczSamochodu.configure(bg="#A5978B")

        myLabel = Label(self.oknoWypozyczSamochodu, text="Wypozycz Samochód", bg="#A5978B", font=("Georgia", 15))
        myLabel.pack()
        myLabel.place(x=108,y=10)

        self.odswiezDropdownMenuWypozycz()

        label_dropdown = Label(self.oknoWypozyczSamochodu, text="Wybierz samochód:", bg="#A5978B", font=("Georgia", 12))
        label_dropdown.pack()
        label_dropdown.place(x=130,y=40)
        

        self.dropdown_samochody = ttk.Combobox(self.oknoWypozyczSamochodu, values=self.samochody_list)
        self.dropdown_samochody.pack()
        self.dropdown_samochody.place(x=130,y=70)

        przycisk_usun = Button(self.oknoWypozyczSamochodu, text="Wypozycz samochód", command=self.WypozyczWybranySamochod, bg="#E7D1BE", font=("Georgia", 12))
        przycisk_usun.pack()
        przycisk_usun.place(x=127,y=100)


    def WypozyczWybranySamochod(self):
        wybrany_samochod = self.dropdown_samochody.get()
        id_samochodu = wybrany_samochod.split(" - ")[0]  # Pobierz ID samochodu z tekstu
        print("IDSAMOCHODU----",id_samochodu)

        cur = self.baza.conn.cursor()
        sql = "UPDATE Samochody SET dostepnosc = 'Wypozyczony' WHERE ID = %s"
        cur.execute(sql, (id_samochodu,))
        self.baza.conn.commit()
        cur.close()


        print("Samochód został Wypozyczony")
        self.oknoWypozyczSamochodu.withdraw()
        
    def odswiezDropdownMenuWypozycz(self):
        samochody = self.baza.wyswietlWszystkieSamochody()
        if samochody is not None:
            self.samochody_list = [
                f"{samochod[7]} - {samochod[0]} {samochod[2]}"
                for samochod in samochody
                if samochod[8] == "Zarezerwowany" 
            ]
            print(self.samochody_list)
        else:
            print("Błąd podczas pobierania danych.")

#Oddawanie
    def OddajSamochod(self):
        self.oknoOddajSamochodu = Toplevel(self.okno)
        self.oknoOddajSamochodu.geometry("400x200")
        self.oknoOddajSamochodu.configure(bg="#A5978B")

        myLabel = Label(self.oknoOddajSamochodu, text="Oddaj Samochód", bg="#A5978B", font=("Georgia", 15))
        myLabel.pack()
        myLabel.place(x=120,y=10)

        self.odswiezDropdownMenuOddaj()

        label_dropdown = Label(self.oknoOddajSamochodu, text="Wybierz samochód:", bg="#A5978B", font=("Georgia", 12))
        label_dropdown.pack()
        label_dropdown.place(x=130, y=40)
     
        self.dropdown_samochody = ttk.Combobox(self.oknoOddajSamochodu, values=self.samochody_list)
        self.dropdown_samochody.pack()
        self.dropdown_samochody.place(x=130,y=70)

        przycisk_usun = Button(self.oknoOddajSamochodu, text="Oddaj samochód", command=self.OddajWybranySamochod, bg="#E7D1BE", font=("Georgia", 12))
        przycisk_usun.pack()
        przycisk_usun.place(x=135,y=100)


    def OddajWybranySamochod(self):
        wybrany_samochod = self.dropdown_samochody.get()
        id_samochodu = wybrany_samochod.split(" - ")[0]  # Pobierz ID samochodu z tekstu
        print("IDSAMOCHODU----", id_samochodu)

        cur = self.baza.conn.cursor()
        sql = "UPDATE Samochody SET dostepnosc = 'Dostępny' WHERE ID = %s"
        cur.execute(sql, (id_samochodu,))
        self.baza.conn.commit()
        cur.close()


        print("Samochód został Oddany")
        self.oknoOddajSamochodu.withdraw()


    def odswiezDropdownMenuOddaj(self):
        samochody = self.baza.wyswietlWszystkieSamochody()
        if samochody is not None:
            self.samochody_list = [
            f"{samochod[7]} - {samochod[0]} {samochod[2]}"
            for samochod in samochody
            if samochod[8] == "Wypozyczony"
            ]
            print(self.samochody_list)
        else:
            print("Błąd podczas pobierania danych.")





if __name__ == "__main__":
    aplikacja = Pracownik()
    aplikacja.okno.mainloop()

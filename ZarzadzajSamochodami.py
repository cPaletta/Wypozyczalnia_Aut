from bazaSamochodow import bazaSamochodow
import psycopg2
import tkinter as tk
from tkinter import *
from tkinter import ttk


class ZarzadzajSamochodami:
    def __init__(self, okno):
        self.okno = okno  
        self.baza = bazaSamochodow()
    def usunSamochod(self):
        self.oknoUsunieciaSamochodu = Toplevel(self.okno)
        self.oknoUsunieciaSamochodu.geometry("500x500")
        self.oknoUsunieciaSamochodu.configure(bg="#708090")

        myLabel = Label(self.oknoUsunieciaSamochodu, text="Usun samochod", bg="#708090")
        myLabel.pack()

        self.odswiezDropdownMenu()

        label_dropdown = Label(self.oknoUsunieciaSamochodu, text="Wybierz samochód:")
        label_dropdown.pack()

        self.dropdown_samochody = ttk.Combobox(self.oknoUsunieciaSamochodu, values=self.samochody_list)
        self.dropdown_samochody.pack()

        przycisk_usun = Button(self.oknoUsunieciaSamochodu, text="Usuń samochód", command=self.usunWybranySamochod)
        przycisk_usun.pack()

    def usunWybranySamochod(self):
        wybrany_samochod = self.dropdown_samochody.get()
        id_samochodu = wybrany_samochod.split(" - ")[0]  # Pobierz ID samochodu z tekstu
        print("IDSAMOCHODU----",id_samochodu)

        cur = self.baza.conn.cursor()
        sql = "DELETE FROM Samochody WHERE ID = %s"
        cur.execute(sql, (id_samochodu,))
        self.baza.conn.commit()
        cur.close()

        print("Samochód usunięty z bazy danych.")
        self.oknoUsunieciaSamochodu.withdraw()

    def odswiezDropdownMenu(self):
        samochody = self.baza.wyswietlWszystkieSamochody()
        if samochody is not None:
            self.samochody_list = [f"{samochod[7]} - {samochod[0]} {samochod[2]}" for samochod in samochody]
            print(self.samochody_list)
        else:
            print("Błąd podczas pobierania danych.")


    def dodajSamochod(self):    
        self.oknoDodaniaSamochodu = Toplevel(self.okno)
        self.oknoDodaniaSamochodu.geometry("500x500")
        self.oknoDodaniaSamochodu.configure(bg="#708090")

        myLabel = Label(self.oknoDodaniaSamochodu, text="Dodaj samochod", bg="#708090")
        myLabel.pack()

        # Etykieta i pole dla marki samochodu
        label_marka = Label(self.oknoDodaniaSamochodu, text="Marka:")
        label_marka.pack()
        self.wejscieMarka = Entry(self.oknoDodaniaSamochodu)
        self.wejscieMarka.pack()

        # Etykieta i pole dla kategorii samochodu
        label_kategoria = Label(self.oknoDodaniaSamochodu, text="Kategoria:")
        label_kategoria.pack()
        self.wejscieKategoria = Entry(self.oknoDodaniaSamochodu)
        self.wejscieKategoria.pack()

        # Etykieta i pole dla modelu samochodu
        label_model = Label(self.oknoDodaniaSamochodu, text="Model:")
        label_model.pack()
        self.wejscieModel = Entry(self.oknoDodaniaSamochodu)
        self.wejscieModel.pack()

        # Etykieta i pole dla VIN samochodu
        label_vin = Label(self.oknoDodaniaSamochodu, text="VIN:")
        label_vin.pack()
        self.wejscieVin = Entry(self.oknoDodaniaSamochodu)
        self.wejscieVin.pack()

        # Etykieta i pole dla numeru rejestracyjnego samochodu
        label_nr_rejestracyjny = Label(self.oknoDodaniaSamochodu, text="Nr Rejestracyjny:")
        label_nr_rejestracyjny.pack()
        self.wejscieNrRejestracyjny = Entry(self.oknoDodaniaSamochodu)
        self.wejscieNrRejestracyjny.pack()

        # Etykieta i pole dla opisu samochodu
        label_opis = Label(self.oknoDodaniaSamochodu, text="Opis:")
        label_opis.pack()
        self.wejscieOpis = Entry(self.oknoDodaniaSamochodu)
        self.wejscieOpis.pack()

        # Etykieta i pole dla historii samochodu
        label_historia = Label(self.oknoDodaniaSamochodu, text="Historia:")
        label_historia.pack()
        self.wejscieHistoria = Entry(self.oknoDodaniaSamochodu)
        self.wejscieHistoria.pack()

        # Etykieta i pole dla dostępności samochodu
        label_dostepnosc = Label(self.oknoDodaniaSamochodu, text="Dostępność:")
        label_dostepnosc.pack()
        self.wejscieDostepnosc = Entry(self.oknoDodaniaSamochodu)
        self.wejscieDostepnosc.pack()

        przyciskDodaniaSamochodu = Button(self.oknoDodaniaSamochodu, text="Dodaj samochód", command=self.zapiszSamochod)
        przyciskDodaniaSamochodu.pack()

    def zapiszSamochod(self):
        marka = self.wejscieMarka.get()
        kategoria = self.wejscieKategoria.get()
        model = self.wejscieModel.get()
        vin = self.wejscieVin.get()
        nr_rejestracyjny = self.wejscieNrRejestracyjny.get()
        opis = self.wejscieOpis.get()
        historia = self.wejscieHistoria.get()
        dostepnosc = self.wejscieDostepnosc.get()

        try:
            # Open a new connection for adding a car
            new_conn = psycopg2.connect(
                user="postgres",
                host="localhost",
                database="Wypozyczalnia",
                password="qwerty",
                port=5432,
            )
            cur = new_conn.cursor()
            sql = "INSERT INTO Samochody (MarkaSamochodu, KategoriaSamochodu, ModelSamochodu, VIN, nrRejestracyjny, OpisSamochodu, Historia, Dostepnosc) " \
                "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
            values = (marka, kategoria, model, vin, nr_rejestracyjny, opis, historia, dostepnosc)
            cur.execute(sql, values)
            new_conn.commit()
            print("Samochód dodany do bazy danych.")
        except Exception as e:
            print(f"Błąd podczas dodawania samochodu do bazy danych: {e}")
        finally:
            if cur is not None:
                cur.close()
            if new_conn is not None and not new_conn.closed:
                new_conn.close()

        self.oknoDodaniaSamochodu.withdraw()
        print(marka, kategoria, model, vin, nr_rejestracyjny, opis, historia, dostepnosc)


    


if __name__ == "__main__":
    aplikacja = ZarzadzajSamochodami()
    aplikacja.okno.mainloop()

        
    


from tkinter import *
import tkinter as tk
from tkinter import ttk
import psycopg2
from bazaUzytkownikow import bazaUzytkownikow


class ZarzadzajOsobami:
    def __init__(self, okno):
        self.okno = okno  
        self.baza = bazaUzytkownikow()

    def usunOsobe(self):
        self.oknoUsunieciaOsoby = Toplevel(self.okno)
        self.oknoUsunieciaOsoby.geometry("500x200")
        self.oknoUsunieciaOsoby.configure(bg="#A5978B")

        myLabel = Label(self.oknoUsunieciaOsoby, text="Usuń użytkownika", bg="#A5978B", font=("Georgia", 20))
        myLabel.pack()
       

        self.odswiezDropdownMenu()

        label_dropdown = Label(self.oknoUsunieciaOsoby, text="Wybierz osobę:", bg="#A5978B", font=("Georgia", 12))
        label_dropdown.pack()

        self.dropdown_osoby = ttk.Combobox(self.oknoUsunieciaOsoby, values=self.osoby_list, font=("Georgia", 12))
        self.dropdown_osoby.pack()

        przycisk_usun = Button(self.oknoUsunieciaOsoby, text="Usuń osobę", command=self.usunWybranaOsobe, bg="white", font=("Georgia", 12))
        przycisk_usun.pack()

    def usunWybranaOsobe(self):
        wybrana_osoba = self.dropdown_osoby.get()
        id_osoby = wybrana_osoba.split(" - ")[0]  # Pobierz ID osoby z tekstu
        print("IDOSOBY----", id_osoby)

        cur = self.baza.conn.cursor()
        sql = "DELETE FROM Klienci WHERE ID = %s"
        cur.execute(sql, (id_osoby,))
        self.baza.conn.commit()
        cur.close()

        print("Osoba usunięta z bazy danych.")
        self.oknoUsunieciaOsoby.withdraw()

    def odswiezDropdownMenu(self):
        osoby = self.baza.wyswietlWszystkichUzytkownikow()
        if osoby is not None:
            self.osoby_list = [f"{osoba[0]} - {osoba[3]} {osoba[4]}" for osoba in osoby]
            print(self.osoby_list)
        else:
            print("Błąd podczas pobierania danych.")

    def dodajOsobe(self):
        self.oknoDodaniaOsoby = Toplevel(self.okno)
        self.oknoDodaniaOsoby.geometry("500x500")
        self.oknoDodaniaOsoby.configure(bg="#A5978B")

        myLabel = Label(self.oknoDodaniaOsoby, text="Dodaj osobę", bg="#A5978B", font=("Georgia", 12))
        myLabel.pack()

        labels = ["Nazwa użytkownika:", "Hasło:", "Imię:", "Nazwisko:", "Liczba wypożyczonych samochodów:", "Pesel:", "Numer telefonu:"]
        entries = []
        for label_text in labels:
            label = Label(self.oknoDodaniaOsoby, text=label_text, bg="#A5978B", font=("Georgia", 12))
            label.pack()
            entry = Entry(self.oknoDodaniaOsoby, bg="#A5978B", font=("Georgia", 12))
            entry.pack()
            entries.append(entry)

        przyciskDodaniaOsoby = Button(self.oknoDodaniaOsoby, text="Dodaj osobę", command=lambda: self.zapiszOsobe(entries), bg="#A5978B", font=("Georgia", 12))
        przyciskDodaniaOsoby.pack()

    def zapiszOsobe(self, entries):
        values = [entry.get() for entry in entries]

        try:
            new_conn = psycopg2.connect(
                user="postgres",
                host="localhost",
                database="Wypozyczalnia",
                password="qwerty",
                port=5432,
            )
            cur = new_conn.cursor()
            sql = "INSERT INTO Klienci (nazwaUzytkownika, Haslo, Imie, Nazwisko, LiczbaWypozyczonychSamochodow, Pesel, NumerTelefonu) " \
                "VALUES (%s, %s, %s, %s, %s, %s, %s)"
            cur.execute(sql, tuple(values))
            new_conn.commit()
            print("Osoba dodana do bazy danych.")
        except Exception as e:
            print(f"Błąd podczas dodawania osoby do bazy danych: {e}")
        finally:
            if cur is not None:
                cur.close()
            if new_conn is not None and not new_conn.closed:
                new_conn.close()

        self.oknoDodaniaOsoby.withdraw()


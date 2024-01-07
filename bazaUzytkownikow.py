import psycopg2
import tkinter as tk
class bazaUzytkownikow:
    def __init__(self):
        self.conn = psycopg2.connect(
            user="postgres",
            host="localhost",
            database="Wypozyczalnia",
            password="qwerty",
            port=5432
        )

    def wyswietlWszystkichUzytkownikow(self):
        try:
            cur = self.conn.cursor()
            cur.execute("SELECT * FROM Klienci")
            rows = cur.fetchall()
            print(rows[0])
            for row in rows:
                print(row)
            cur.close()
            return rows
        except Exception as e:
            print(f"Błąd podczas wyświetlania danych: {e}")
            return None
    

    def dodajUzytkownika(self, uzytkownik, haslo, imie, nazwisko, liczba_wypozyczonych_samochodow, pesel, numer_telefonu):
        try:
            cur = self.conn.cursor()
            sql = "INSERT INTO Klienci (nazwaUzytkownika, Haslo, Imie, Nazwisko, LiczbaWypozyczonychSamochodow, Pesel, NumerTelefonu) " \
                "VALUES (%s, %s, %s, %s, %s, %s, %s)"
            values = (uzytkownik, haslo, imie, nazwisko, liczba_wypozyczonych_samochodow, pesel, numer_telefonu)
            cur.execute(sql, values)
            self.conn.commit()
            print("Użytkownik dodany do bazy danych.")
            return 1
        except Exception as e:
            print(f"Błąd podczas dodawania użytkownika do bazy danych: {e}")
            return 0
        finally:
            self.conn.close()

    def Walidacja(self, uzytkownik, haslo):
        try:
            cur = self.conn.cursor()
            sql = "SELECT * FROM Klienci WHERE nazwaUzytkownika = %s AND Haslo = %s;"
            values = (uzytkownik, haslo)
            cur.execute(sql, values)
            rows = cur.fetchall()
            if rows:
                print("Użytkownik istnieje w bazie danych.")
            else:
                print("Użytkownik nie istnieje w bazie danych.")
            return rows
        except Exception as e:
            print(f"Błąd podczas walidacji użytkownika: {e}")
        finally:
            cur.close()
            self.conn.close()

    def zmianaDanych(self, uzytkownik, haslo, imie, nazwisko, pesel, numer_telefonu, idUzytkownika):
        try:
            cur = self.conn.cursor()
            sql = "UPDATE Klienci SET nazwaUzytkownika = %s, Haslo = %s, Imie = %s, Nazwisko = %s,  Pesel = %s, NumerTelefonu = %s WHERE ID = %s;"
            values = (uzytkownik, haslo, imie, nazwisko, pesel, numer_telefonu, idUzytkownika)
            cur.execute(sql, values)
            self.conn.commit()
            print("Dane użytkownika zaktualizowane.")
            return values
        except Exception as e:
            print(f"Błąd podczas aktualizacji danych użytkownika: {e}")
            return 0
        finally:
            cur.close()
            self.conn.close()
    
        



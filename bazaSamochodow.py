import psycopg2

class bazaSamochodow:
    def __init__(self):
        self.conn = psycopg2.connect(
            user= "postgres",
            host= "localhost",
            database= "Wypozyczalnia",
            password= "qwerty",
            port= 5432,
            
        )

    def wyswietlWszystkieSamochody(self):
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM Samochody")
        rows = cur.fetchall()
        cur.close()
        return rows
    
    def wyswietlanieRezerwacji(self):
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM rezerwacje")
        rows = cur.fetchall()
        cur.close()
        return rows
    

    def zamknij_polaczenie(self):
        self.conn.close()
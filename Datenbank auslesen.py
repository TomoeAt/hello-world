import os
import mysql.connector as mariadb
# Klasse Anmeldung an Datenbank erstellen, mit Methode anmelden, Attributen, Benutzer, Password , Benutzerverwaltug)

class Anmeldung_an_Datenbank:

    def __init__(self, user, password, database):  # Konstruktor zum Erzeugen von Objekt
        self.user = Nutzer
        self.password = Password
        self.database = Datenbank

    def myLogging(self, logtext):
        file = open('log.txt', 'a')
        file.write(logtext)
        file.close

    def nutzer_anlegen(self,test):
        # username = username aus Datenbank muss unten dann eingefuegt werden
        # test = new_user  # input("Benutzername:")
        new_pwd = "1234"
        os.system("useradd -d /home/" + test + " -m " + test + " -p " + new_pwd)
        print(test)
        # Benutzer wird angelegt Passwort wird auch angelegt
        logtext= 'Benutzer erfolgreich anglegt.\n'
        self.myLogging(logtext)


    def Anmelden(self):
        mariadb_connection = mariadb.connect(user=self.user, password=self.password, database=self.database)
        cursor = mariadb_connection.cursor()
        logtext = 'Erfolgreich an Datenbank angemeldet.\n'
        self.myLogging(logtext)
        cursor.execute("SELECT * FROM Benutzer")
        result = cursor.fetchall()
        l =len(result)
        for r in result:
          test = r[1]
          self.nutzer_anlegen(test)
          logtext = 'Daten erfolgreich ausgelesen \n'
          self.myLogging(logtext)

          mariadb_connection.close()



# Nutzerdateneingabe
Nutzer = 'admin' #input("Benutzername:")
Password = '1234'#input("Passwort:")
Datenbank = 'Benutzerverwaltung'#input("Datenbank:")


x = Anmeldung_an_Datenbank(Nutzer, Password, Datenbank)  # Erstellung eines Objektes der Klasse
x.Anmelden()  # Funktion aufrufen
print(x.password)  # Password des Objektes x der Klasse Anmeldung an Datenbank ausgeben.import os






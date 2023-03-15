import time
from objekt import *
from raum import *
from spieler import *

erste_strasse = Raum("erste Teststrasse", "Eine Teststrasse")

zweite_strasse = Raum("zweite Teststrasse", "Eine weitere Teststrasse", False)

testobjekt = Objekt("Testobjekt", "Das ist ein Testobjekt der ist fuer die zweite Teststrasse gemeint. Benutze ihn um den Weg zu verschaffen.")

testobjekt2 = Objekt("Testobjekt2", "Das ist kein Testobjekt der ist fuer die zweite Teststrasse gemeint. Benutze ihn einfach so...")

erste_strasse.objektliste.append(testobjekt)
erste_strasse.objektliste.append(testobjekt2)
erste_strasse.westen = zweite_strasse

zweite_strasse.oeffnungsobjekt = testobjekt

spieler = Spieler(erste_strasse, [], 4)

print("Am besten bitte direkt am Anfang des Spiels den Befehl 'hilfe' eingeben und alle Moeglichkeiten merken oder aufzuschreiben.")
time.sleep(2)

# Start der Spielschleife
while True:
    if not spieler.raum.name == "Auf der Sitzbank":
        spieler.umschauen()

        aktion = input("Was möchtest du tun? \n")
        aktionsteile = aktion.lower().split(" ")

        if aktionsteile[0] == "gehe":
            if len(aktionsteile) > 1:
                spieler.bewegen(aktionsteile[1])
            else:
                richtung = input("Nennst du mir bitte die Richtung: \n")
                spieler.bewegen(richtung.lower())
        elif aktionsteile[0] == "nimm":
            if len(aktionsteile) > 1:
                spieler.mitnehmen(aktionsteile[1])
            else:
                objekt = input("Nennst du mir bitte den Objekt: \n")
                spieler.mitnehmen(objekt.lower())
        elif aktionsteile[0] == "lege":
            if len(aktionsteile) > 1:
                spieler.ablegen(aktionsteile[1])
            else:
                objekt = input("Nennst du mir bitte den Objekt: \n")
                spieler.mitnehmen(objekt.lower())
        elif aktionsteile[0] == "benutze":
            if len(aktionsteile) > 1:
                spieler.einsetzen(aktionsteile[1])
            else:
                objekt = input("Nennst du mir bitte den Objekt: \n")
                spieler.mitnehmen(objekt.lower())
        elif aktionsteile[0] == "hilfe":
            print("Du kannst folgende Befehle benutzen:\n"
                  "- gehe (Richtung(Es gibt: Norden, Sueden, Osten, Westen, Oben, Unten)) \n"
                  "- nimm (Name des Objekts) \n"
                  "- lege (Name des Objekts) \n"
                  "- benutze (Name des Objekts) \n"
                  "Es werden keine Umlaute benutzt.")
        elif aktionsteile[0] == "gewonnen" and spieler.raum.name == "zweite Teststrasse":
            print("Dies ist das Ende, du hast endlich dein Ziel erreicht... Viel Glueck! \n"
                  "Ich hoffe das Spiel hat richtig funktioniert und es gab keine Fehlermeldungen :)")
            break
        else:
            print("Ich verstehe nicht was du meinst.")
    else:
        print("Dies ist das Ende, du hast endlich dein Ziel erreicht... Viel Glueck! \n"
              "Ich hoffe das Spiel hat richtig funktioniert und es gab keine Fehlermeldungen :)")
        break

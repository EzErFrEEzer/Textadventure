import time
from objekt import *
from raum import *
from spieler import *

# Objekte der Klasse 'Raum'

erste_strasse = Raum("Erste Strasse",
                     "Das ist die erste Strasse der Stadt Slavberg, deswegen ist die auch so genannt: Erste Strasse")

danilov_strasse = Raum("Danilov Strasse",
                       "Hier wohnt ein Freund von dir, sein Nachname ist zufaelligerweise auch Danilov. "
                       "Ihr hattet eine Verabredung. Du siehst ihm schon neben der Sitzbank stehen,"
                       "er versucht mit Schreien dir irgendetwas zu sagen.")

neben_der_sitzbank = Raum("Neben der Sitzbank",
                          "Dein Freund sagt dir folgendes: 'Hast du nicht zugehoert, "
                          "ich habe doch das Schluessel zu meiner Wohnung an dich geworfen. "
                          "Hol mir meine beliebteste Josuke-Figur, bitte.'")

haus_37_e = Raum("Haus № 37 Eingang",
                 "Das ist ein vierstoeckiges Haus. In diesem haus wohnt dein Freund.")

haus_37_erd = Raum("Erdgeschoss des Hauses № 37",
                   "Du sieht einen Aufzug. Das wird schnell sein. Der kommt aber nicht. 'Dann kommt die Treppe...'")

haus_37_keller = Raum("Keller des Hauses № 37",
                      "Du siehst einen Skelett-model? Ausserdem ist hier dunkel, "
                      "aber genau dafuer hast du ja diese Taschenlampe, die du gefunden hast.",
                      False)

haus_37_1 = Raum("1. Stock des Hauses № 37",
                 "Dein Freund wohnt auf diesen Stock. Es war die Wohnung 1.2(Richtung Osten). "
                 "Hast du denn den Schluessel ueberhaupt mit?")

wohnung_1_2_e = Raum("Wohnung deines Freundes Eingangsbereich (Wohnung 1.2)",
                     "Hier ist der Eingangsbereich des Wohnung deines Freundes. "
                     "Dein Freund wollte irgendetwas haben also musst du die Wohnung durchschauen.",
                     False)

wohnung_1_2_k = Raum("Kueche deines Freundes",
                     "Es ist nicht das Beste, aber man kann hier essen.")

wohnung_1_2_b = Raum("Badezimmer deines Freundes",
                     "'Wieso bin ich hier ueberhaupt?' - denkst du dich... Wirklich was machst du hier...")

wohnung_1_2_g = Raum("Gaestezimmer deines Freundes",
                     "Hier sollte irgendwo die Figur sein, die ist aber nicht hier... "
                     "Vielleicht hat dieser Zettel damit etwas zu tun.")

haus_37_2 = Raum("2. Stock des Hauses № 37",
                 "Das Maedchen ist schon da und du zeigst ihr den Zettel. Sasha: "
                 "'Ah, ich hab dich gar nicht erwartet. Na ja ich habe die Figur ganz oben am Dach liegen lassen.'",
                 False)

haus_37_3 = Raum("3. Stock des Hauses № 37",
                 "Oh man! Warum wurde die Figur auf dem Dach versteckt?")

haus_37_4 = Raum("4. Stock des Hauses № 37",
                 "Es gibt nichts mehr anderes hier, doch es waere gut nach dem du Figur abholst den Aufzug nehmen.")

aufzug = Raum("Der Aufzug des Hauses № 37",
              "Die Aufzugtaste sah eingeklemmt aus, kommt es ueberhaupt nach unten?")

haus_37_dach = Raum("Dach des Hauses № 37",
                    "Das ist der Dach und hier ist die Figur... Du siehst einen Paar. Was machen die hier. "
                    "Waren die beide hier eingeschlossen? Lieber, die beide nicht zu stoeren.",
                    False)

sitzbank = Raum("Auf der Sitzbank",
                "",
                False)

# Hier werden die Verbindungen der Nachbarräume erstellt.

erste_strasse.sueden = danilov_strasse
danilov_strasse.norden = erste_strasse
danilov_strasse.osten = haus_37_e
danilov_strasse.sueden = neben_der_sitzbank
neben_der_sitzbank.norden = danilov_strasse
neben_der_sitzbank.osten = sitzbank
haus_37_e.westen = danilov_strasse
haus_37_e.osten = haus_37_erd
haus_37_erd.westen = haus_37_e
haus_37_erd.oben = haus_37_1
haus_37_erd.unten = haus_37_keller
haus_37_1.unten = haus_37_erd
haus_37_1.oben = haus_37_2
haus_37_1.osten = wohnung_1_2_e
wohnung_1_2_e.norden = wohnung_1_2_b
wohnung_1_2_e.osten = wohnung_1_2_g
wohnung_1_2_e.sueden = wohnung_1_2_k
wohnung_1_2_e.westen = haus_37_1
wohnung_1_2_b.sueden = wohnung_1_2_e
wohnung_1_2_k.norden = wohnung_1_2_e
wohnung_1_2_g.westen = wohnung_1_2_e
haus_37_2.oben = haus_37_3
haus_37_2.unten = haus_37_1
haus_37_3.oben = haus_37_4
haus_37_4.sueden = aufzug
haus_37_4.oben = haus_37_dach
aufzug.norden = haus_37_4
aufzug.unten = haus_37_erd
haus_37_dach.unten = haus_37_4

# Objekte der Klasse 'Objekt'

k_w_1_2 = Objekt("Schluessel",
                 "Es ist die Nummer 1.2 eingraviert. In der wohnt dein Freund.")

k_dach = Objekt("Dachschluessel",
                "Ist bestimmt fuer den Dach, steht auch auf dem aufgeklebten Zettel.")

taschenlampe = Objekt("Taschenlampe",
                      "Ist bestimmt fuer die Dunkle plaetze gemeint")

zettel = Objekt("Zettel",
                "Auf dem Zettel steht:\n"
                "'Moin, hier ist Sasha die Tuer war offen,\n"
                "ich hab irgendwo dein Figur versteckt :).\n"
                "Komm hoch ich helfe dir. Ich warte auf\n"
                "dich im zweiten Stock!'\n"
                "")

seife = Objekt("Seife",
               "Dein bester Freund beim Haende waschen!...und der schlimmster Feind deiner Augen!")

gabel = Objekt("Gabel",
               "Dein erster bester Freund beim essen!")

teller = Objekt("Teller",
                "Schmutzig, aber man kann es ueberleben.")

messer = Objekt("Messer",
                "Dein zweiter bester Freund beim essen!")

j_figur = Objekt("Josuke-Figur",
                 "Endlich hast du die, jetzt schnell nach unten.")

# Hier werden die Objekte in die Räume eingefügt

danilov_strasse.objektliste.append(k_w_1_2)
wohnung_1_2_k.objektliste.append(gabel)
wohnung_1_2_k.objektliste.append(messer)
wohnung_1_2_k.objektliste.append(teller)
haus_37_keller.objektliste.append(k_dach)
wohnung_1_2_b.objektliste.append(seife)
wohnung_1_2_g.objektliste.append(zettel)
haus_37_erd.objektliste.append(taschenlampe)
haus_37_dach.objektliste.append(j_figur)

# Hier werden die Öffnungsobjekte für die geschlossene Räume ernannt.

haus_37_keller.oeffnungsobjekt = taschenlampe
wohnung_1_2_e.oeffnungsobjekt = k_w_1_2
haus_37_2.oeffnungsobjekt = zettel
haus_37_dach.oeffnungsobjekt = k_dach
sitzbank.oeffnungsobjekt = j_figur

# Hier wird der Spieler erstellt

spieler = Spieler(erste_strasse, [], 4)

# Warnungen vor dem eigentlichen Spiel

print("Am besten bitte direkt am Anfang des Spiels den Befehl 'hilfe' "
      "eingeben und alle Moeglichkeiten merken oder aufzuschreiben.")
print("!!!Wenn das Spiel abgebrochen wird muss man von Vorne anfangen!!!")
time.sleep(2)

# Spielschleife

while True:
    if not spieler.raum.name == "Auf der Sitzbank":
        spieler.umschauen()

        aktion = input("Was moechtest du tun? \n")
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
                  "Es werden keine Umlaute benutzt. Die werden mit 'ae', 'oe' und 'ue' ersetzt.")
        else:
            print("Ich verstehe nicht, was du meinst.")
    else:
        print(f"Dies ist das Ende, du hast endlich dein Ziel erreicht... Viel Glueck, {spieler.name}! \n"
              "Ich hoffe das Spiel hat richtig funktioniert und es gab keine Fehlermeldungen :)")
        break

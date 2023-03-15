import random


class Spieler:
    def __init__(self, raum, inventar, inventar_cap):
        self.name = input("Gib deinen Namen ein: \n")
        self.raum = raum
        self.inventar = inventar
        self.inventar_cap = inventar_cap

    def bewegen(self, richtung):
        raum_neu = self.raum.get_ausgang(richtung)
        if raum_neu is None:
            ausgaben = ["Das kannst du vergessen. Da gibt es nichts interessantes.",
                        "Du wolltest etwas anderes machen. Du kehrst zurueck.",
                        "Es ist leider nicht moeglich. Wolltest du vielleicht in die andere Richtung?"]
            auswahl = random.randint(0, 2)
            print(ausgaben[auswahl])
        else:
            check_offen = raum_neu.offen
            if not check_offen:
                print("Das kannst du vergessen. Du kannst nicht durch. Du brauchst noch irgendetwas.")
            else:
                self.raum = raum_neu

    def mitnehmen(self, obj_name):
        obj = next((obj for obj in self.raum.objektliste if obj.name.lower() == obj_name), None)
        if obj:
            if len(self.inventar) >= self.inventar_cap:
                ausgaben = ["Du hast zu viel Sachen mit.",
                            "Du nimmst es mit..., leider hast keinen Rucksack mit und legst es wieder ab.",
                            "Dein Inventar ist voll."]
                auswahl = random.choice(ausgaben)
                print(auswahl)
            else:
                self.inventar.append(obj)
                self.raum.objektliste.remove(obj)
                print(f"Du nimmst {obj.name} mit. {obj.beschreibung}")
        else:
            print(f"Du siehst hier kein {obj_name} hier.")

    def ablegen(self, obj_name):
        obj = next((obj for obj in self.inventar if obj.name.lower() == obj_name), None)
        if obj:
            self.inventar.remove(obj)
            self.raum.objektliste.append(obj)
            print(f"Du legst {obj.name} vorsichtig auf dem Boden.")
        else:
            print(f"Du hast {obj_name} nicht mit.")

    def umschauen(self):
        print(f"Dein Standort: {self.raum.name}")
        print(self.raum.beschreibung)
        self.raum.get_info()
        if self.raum.objektliste:
            print("Hier gibt es verschiedene Sachen:")
            for obj in self.raum.objektliste:
                print(f"- {obj.name}")
        if self.inventar:
            print("Das hast du mit:")
            for obj in self.inventar:
                print(f"- {obj.name}")
        if not self.raum.objektliste and not self.inventar:
            print("Es gibt hier keine Objekte...")

    def einsetzen(self, obj_name):
        obj = next((obj for obj in self.inventar if obj.name.lower() == obj_name), None)
        if obj:
            richtungen = ["norden", "sueden", "westen", "osten", "oben", "unten"]
            for richtung in richtungen:
                room = self.raum.get_ausgang(richtung)
                if room and obj.name == room.oeffnungsobjekt.name:
                    print(f"Du kannst den Weg zu {room.name} in Richtung {richtung.capitalize()} nehmen.")
                    room.offen = True
                    self.inventar.remove(obj)
                    return
        print("Entweder hast du dieses Objekt nicht mit..., \n"
              "oder alle Wege sind frei..., \n"
              "oder du musst etwas anderes benutzen.")

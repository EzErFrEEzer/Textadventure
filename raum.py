class Raum:
    def __init__(self, name, beschreibung, offen = True):
        self.name = name
        self.beschreibung = beschreibung
        self.objektliste = []
        self.norden = None
        self.sueden = None
        self.osten = None
        self.westen = None
        self.oben = None
        self.unten = None
        self.offen = offen
        self.oeffnungsobjekt = None

    def get_info(self):
        if self.norden:
            print(f"In Richtung Norden: {self.norden.name}")
        if self.sueden:
            print(f"In Richtung Sueden: {self.sueden.name}")
        if self.osten:
            print(f"In Richtung Osten: {self.osten.name}")
        if self.westen:
            print(f"In Richtung Westen: {self.westen.name}")
        if self.oben:
            print(f"Oben gibt es: {self.oben.name}")
        if self.unten:
            print(f"Unten gibt es: {self.unten.name}")

    def set_oeffnungsobjekt(self, obj):
        self.oeffnungsobjekt = obj.name.lower()

    def get_ausgang(self, richtung):
        if richtung == "norden" or richtung == "sueden" or richtung == "osten" or richtung == "westen" \
           or richtung == "oben" or richtung == "unten":
            return getattr(self, richtung)

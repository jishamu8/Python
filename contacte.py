class Contacte:
    def __init__(self,nom, cognoms, mobil):
        self.nom = nom
        self.cognoms = cognoms
        self.mobil = mobil
        self.mail = ""
    
    def toString(self):
        return self.nom + ""  + self.cognoms + "" + self.mobil
class Contacte:
    def __init__(self,nom, cognoms, mobil):
        self.nom = nom
        self.cognoms = cognoms
        self.mobil = mobil
        self.mail = ""
    
    def toString(self):
        return self.nom + " "  + self.cognoms + " " + self.mobil

    def mostrar(self):
        print("Nom del contacte: " + self.nom)
        print("Cognoms del contacte: " + self.cognoms)
        print("Mobil del contacte: " + self.mobil)
        print("Mail del contacte: " + self.mail)
    
    def guardar(self):
        f=open("contactes.txt", "a")
        f.write(self.nom + "\n")
        f.write(self.cognoms + "\n")
        f.write(self.mobil + "\n")
        f.write(self.mail + "\n")
        f.close

#    def guardar(self, fitxer):

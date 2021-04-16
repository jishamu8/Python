from contacte import Contacte

agenda = []
def presenta():
    print("************************************************")
    print("*programa per gestionar una agenda de contactes*")
    print("************************************************")

def alta():
    n = input("Entra el nom: ")
    cn = input("Entra el cognoms: ")
    t = input("Entra el numero mobil: ")
    c = Contacte(n,cn,t)
    agenda.append(c)

def llistar():
    n = len(agenda)
    for i in range (n):
        c=agenda[i]
        print(str(i+1) + "." + c.toString())

def menu():
        print("\n")
        print("Les opcions desponibles son:\n")
        print("    1. Afegir contacte\n")
        print("    2. Consultar contacte\n")
        print("    3. Esborrar contacte\n")
        print("    4. Llistar contactes\n")
        print("    5. Sortir\n")
        print("\n")
        print("Entreu la vostra opcion:",end="")
        o = int(input())
        return o

def main():
    presenta()
    o = menu()
    while o !=5:
        if o == 1:
            alta()
        if o == 4:
            llistar()
        
        o = menu()
    

    print("Adeu")

main()
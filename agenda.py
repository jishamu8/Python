from contacte import Contacte

agenda = []

def presenta():
    print()
    print("**************************************************")
    print("* Programa per gestionar una agenda de contactes *")
    print("**************************************************")
    print()

def numeric(x):
    n = len(x)
    for i in range(n):
        c = x[i]
        if c.isalpha():
           return False

    return True

def alta():
    
    n = input("Entra el nom: ")
    cn= input("Entra els cognoms: ")
    t = input("Entra el numero de mobil: ")
    while not numeric(t):
        print("ERROR: Has d'escriure un valor numeric")
        t = input("Entra el numero de mobil: ")
        
    c = Contacte(n,cn,t)
    agenda.append(c)

def consulta():
    llistar()
    print()
    q = int(input("Entra el numero de contacte a consultar:"))
    c = agenda[q-1]
    c.mostrar()


def esborrar():
    llistar()
    print()
    q = int(input("Entra el numero de contacte a esborrar:"))
    agenda.pop(q-1)

    

def llistar():
    print()
    print("Aquests son els contactes disponibles:")
    print()
    n = len(agenda)
    for i in range(n):
        c = agenda[i]
        print(str(i+1) + ". " + c.toString())  

def guardar():
    # abans de guardar esborrem tot lo que hi hagi el fitxer
    f = open("contactes.txt","w")
    f.close()

    n = len(agenda)
    for i in range(n):
        c = agenda[i]
        c.guardar()

def carregar():
    f = open("contactes.txt","r")
    c = Contacte("","","")
    i = 0
    while c.carregar(f):
        agenda.append(c) 
        c = Contacte("","","")
        i = i + 1
        
    print("S'han carregat " + str(i) + " contactes")

def ordenar(agenda):
    n = len(agenda)
    for i in range(n):
            for j in range(n):
                    if agenda[i].cognoms < agenda[j].cognoms:
                            aux = agenda[i]
                            agenda[i] = agenda[j]
                            agenda[j] = aux
    return agenda
    

def menu():
    print()
    print("Opcions disponibles:")
    print(" 1. Afegir contacte")
    print(" 2. Consultar contacte")
    print(" 3. Esborrar contacte")
    print(" 4. Llistar contactes")
    print(" 5. Guardar contactes")
    print(" 6. Carregar contactes")
    print(" 7. Ordenar contactes")
    print(" 8. Sortir")
    print()
    print("Entreu la vostra opcio:",end="")
    o = int(input())
    return o


def main():
    carregar()
    presenta()
    o = menu()
    while o != 8:
        if o == 1:
            alta()

        if o == 2:
            consulta()

        if o == 3:
            esborrar()

        if o == 4:
            llistar()

        if o == 5:
            guardar()

        if o == 6:
            carregar()

        if o == 7:
            ordenar()
            
        o = menu()

    r = input("Vols salvar els nous contactes? [def. Si]")
    if len(r) == 0 or r[0] == "S" or r[0] == "s":
        guardar()
    print("Adeu!")


main()



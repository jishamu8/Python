from contacte import Contacte
def menu():
        print("\n")
        print("Les opcions desponibles son:\n")
        print("    1. Afegir contacte\n")
        print("    2. Consultar contacte\n")
        print("    3. Esborrar contacte\n")
        print("    4. Llistar contactes\n")
        print("    5. Guardar contactes\n")
        print("    6. Carregar contactes\n")
        print("    7. Ordenar contactes\n")
        print("    8. Sortir\n")
        print("\n")
        print("Entreu la vostra opcion:",end="")
        o = int(input())
        return o

agenda = []

def presenta():
    print("************************************************")
    print("*Programa per gestionar una agenda de contactes*")
    print("************************************************")

def numeric(x):
    n = len(x)
    for i in range(n):
        c = x[i]
        if c.isalpha():
            return False
    return True


def alta():
    n = input("Entra el nom: ")
    cn = input("Entra el cognoms: ")
    t = input("Entra el numero mobil: ")
    while not numeric(t):
        print("Error!!! Has d'escriure un valor numeric")
        t=input("Entra el numero de mobil: ")

    c = Contacte(n,cn,t)
    agenda.append(c)

def llistar():
    n = len(agenda)
    for i in range (n):
        c=agenda[i]
        print(str(i+1) + ". " + c.toString())

def consulta():
    llistar()
    print("Aquest son el contacte possible")
    q = int(input("Entra el numero de contacte a consultar: "))
    c = agenda[q-1]
    c.mostrar()

def esborrar():
    llistar()
    print()
    q = int(input("Entra el numero de contacte a esborar: "))
    agenda.pop(q-1)

def guardar():
    n = len(agenda)
    f = open("contactes.txt", "w")
    f.close()
    for i in range(n):
        c = agenda[i]
        c.guardar()

def carregar():
    f = open("contactes.txt", "r")
    c = Contacte("","","")
    i = 0

    while c.carregar(f):
        agenda.append(c)
        c = Contacte("","","")
        i = i + 1
    print("S'han carregat " + str(i)+ " contactes")


def ordenar(v):
    n = len(v)
    for i in range(n):
            for j in range(n):
                    if i<j:
#                         si i<j es cierto quiere ecir que el elemento v[i]
#                         es anterior a v[j] -> si además v[i] > v[j]
                            if v[i] > v[j]:
                                    aux = v[i]
                                    v[i] = v[j]
                                    v[j] = aux
    return v

def main():
    carregar()
    presenta()
    o = menu()
    while o !=8:
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
           print(ordenar([3,4,5,1]))
        
        o = menu()
    
    r = input("Vols salvar els nous contactes? [def. Si]")
    if  len(r) == 0 or r[0] == "s" or  r[0] == "S":
        guardar()
    print("Adeu")

main()
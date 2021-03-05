from dau import tirar_dau

def entra_noms(n):
    names = []
    for i in range(n):
        noms=input("Entra el nom del jugador numero " + str(i+1) + ":" )
        names.append(noms)

    return names

def entra_colors(n):
    cols = []
    for i in range(n):
        colors=input("El color del jugador numero " + str(i+1) + ":" )
        cols.append(colors)

    return cols


def menu():
    print("1. Veure posicions")
    print("2. Seguent jugada")
    o=int(input("Entreu opcio: "))
    return o
def posicio_75(posicions):
    n = len (posicions)
    for i in range(n):
        if posicions[i] == 75:
            return True
    return False

def seguent_jugada(posicions, torn, noms, colors):
    print("Torn "+ noms[torn] + " que juga amb el color " + colors[torn])
    print(noms[torn] + " estas a la posicio " + str(posicions[torn]))
    print("prem return per tirar el dau")
    dummy = input()
    numero = tirar_dau()
    posicions[torn] = posicions[torn] + numero
 

def veure_posicions(n):
    for i in range(n):
        print(nom[i] + " esta en la posicio " + str(posicions[i]))


def parchis():
     n=int(input("Quants jugadors hi haura: "))
     noms = entra_noms(n)
     colors = entra_colors(n)

     posicions = []
     for i in range(n):
         posicions.append(0)
    
     torn = 0

     while not posicio_75(posicions):
         opcio= menu()
         if opcio == 1:
             print(posicions)

         if opcio == 2: 
             seguent_jugada(posicions, torn, noms, colors)
             torn = torn + 1
             if torn == n:
                 torn = 0

parchis()
  
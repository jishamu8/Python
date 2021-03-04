from dau import tirar_dau
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

def seguent_jugada(poicions, torn):
    print("prem return per tirar el dau")
    dummy = input()
    numero = tirar_dau()
    posicions[torn] = posicions[torn] + numero


def parchis():
     #n=int(input("Quants jugadors hi haura: "))
     n = 1
     noms = []
     noms.append("Ishamu")
     colors = []
     colors.append("Vermelles")

     posicions = []

     for i in range(n):
         posicions.append(0)
    
     torn = 0

     while not posicio_75(posicions):
         opcio= menu()
         if opcio == 1:
             print(posicions)

         if opcio == 2: 
             seguent_jugada(posicions, torn)
             torn = torn + 1
             if torn == n:
                 torn = 0

parchis()

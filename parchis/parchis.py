from dau import tirar_dau
from entra_numero import entra_numero
 
def entra_noms(n):
 
    names = []
    for i in range(n):
        print("Entra el nom del jugador o jugadora numero " + str(i+1) + ":")
        nom = input()
        names.append(nom)
 
    return names
 
def menu():
    print("1. Veure posicions")
    print("2. Seguent jugada")
    o = entra_numero("Entreu opció:");
    return o
 
def qui_ha_acabat_la_partida(posicions,ha_passat_la_casella_68):
    posicions_inici_pasillos = [0,17,34,51]
    n = len(posicions)
 
    for i in range(n):
        if posicions[i] >= posicions_inici_pasillos[i] + 7 and ha_passat_la_casella_68[i]:
            return i
 
    return -1
 
 
def seguent_jugada(posicions,torn,noms,colors,ha_passat_la_casella_68):
 
    print("Torn de " + noms[torn] + " que juga amb les fitxes " + colors[torn]) 
    print(noms[torn] + " estas a la posicio " +  str(posicions[torn]) + ", ",end="")
    if ha_passat_la_casella_68[torn]:
        print("i ja has passat la casella 68")
    else:
        print("però encara no has passat la casella 68")
 
    print("Prem return per tirar el dau")
    dummy = input()
 
    posicio_antiga = posicions[torn]
    numero = tirar_dau()
    posicio_nova = posicio_antiga + numero
    if posicio_nova > 68:
        ha_passat_la_casella_68[torn] = True
        posicio_nova = posicio_nova - 68
 
    posicions[torn] =  posicio_nova
 
 
def veure_posicions(n,noms,posicions):
    for i in range(n):
        print(noms[i] + " esta a la posicio " + str(posicions[i]))    
 
def parxis():
# n representa el numero de jugadors
    n = int(input("Quants jugadors sereu?"))
    noms = entra_noms(n)
 
    colors = ["grogues","verdes","vermelles","blaves"]
 
    seguros = [5,12,17,22,29,34,39,46,51,56,63,68]
 
    posicions_inicials = [5,22,39,56]
    ha_passat_la_casella_68 = [False,False,False,False]
 
 
    posicions = []
    for i in range(n):
        pi = posicions_inicials[i]
        posicions.append(pi)
 
    torn = 0
    guanyador = qui_ha_acabat_la_partida(posicions,ha_passat_la_casella_68)
    while guanyador == -1 :
        opcio = menu()
        if opcio == 1:
            veure_posicions(n,noms,posicions)
        if opcio == 2:
            seguent_jugada(posicions,torn,noms,colors,ha_passat_la_casella_68)
            torn = torn + 1
            if torn == n:
                torn = 0
 
        guanyador = qui_ha_acabat_la_partida(posicions,ha_passat_la_casella_68)
 
    print("Enhorabona, " + noms[guanyador]+ ", has guanyat la partida!")
 
 
 
parxis()

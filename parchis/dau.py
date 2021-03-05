import random
#n es nombre senar que representa la mida que qualsevol costat del dau 
def construeix_dau(n):
    if n % 2 == 0:
        print ("El nombre de caselles ha de ser senar")
        return
    M = []
    for i in range(n):
        f = []
        for j in range(n):
            f.append(" ")

        M.append(f)

    return M

def pinta_dau(n, numero):
    d = construeix_dau(n)
    
    if numero == 1:
        d[n//2][n//2]="o"
    
    if numero == 2:
        d[0][0] = "o"
        d[n-1][n-1] = "o"

    if numero == 3:
        d[0][0] = "o"
        d[n//2][n//2]="o"
        d[n-1][n-1] = "o"
    
    if numero == 4:
        d[0][0] = "o"
        d[0][n-1] = "o"
        d[n-1][0] = "o"
        d[n-1][n-1] = "o"


    if numero == 5:
        d[0][0] = "o" 
        d[0][n-1] = "o"
        d[n//2][n//2] = "o"
        d[n-1][0] = "o"
        d[n-1][n-1] = "o"

    if numero == 6:
        d[0][0] = "o"
        d[0][n-1] = "o"
        d[n//2][0] = "o"
        d[n//2][n-1] = "o"
        d[n-1][0] = "o"
        d[n-1][n-1] = "o"

    return d
def escriu_dau(d):
    n = len(d)
    for i in range(n):
        print(d[i])

def tirar_dau():
    numero = random.randint(1,6)
    dau = pinta_dau(3,numero)
    escriu_dau(dau)
    return numero
    


def main():
    tirar_dau()

main()

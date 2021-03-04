def paritat():
    numero=int(input("Indica un numero:"))
    if numero % 2 == 0:
        print("Es parell")
    else:
        print("Es senar")

def construir_matriu(n, m):
    M = []
    for i in range (n):
        f=[]
        for j in range(m):
            f.append(0)
        M.append(f)
    return M

def escriure_matriu(M):
    n=len(M)
    m=len(M[0])
    for i in range(m):
        print(M[i])
 
def construir_matriu_quadrada(n):
    return construir_matriu(n,n)


def cinc():
    n = int(input("Entra l'ordre (senar): "))
    M = construir_matriu_quadrada(n)
    M[0][0] = 1
    M[0][n-1] = 1
    M[n-1][0] = 1
    M[n-1][n-1] = 1
    M[n//2][n//2] = 1


    escriure_matriu(M)
 
def identitat():
    n = int(input("Entra l'ordre (senar): "))
    for i in range (n):
        for j in range(n):
            if  i == j:
                 (M[i][j])=1

def main():
    #matriu = construir_matriu(3,5)
    #print(matriu)
    #M = [[1,2], [3,4]]
    #cinc()
    identitat()
main()

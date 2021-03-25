from random import randint
 
# construeix_dau() reb la mida (nombre de caselles del dau, que ha de ser senar
# i retorna la matriu que és la imatge del dau, però tota en blancs.
 
# n es un nombre senar que representa la mida de qualsevol costat del dau
def construeix_dau(n):
    if n % 2 == 0:
        print("El nombre de caselles ha de ser senar")
        return
 
    M = []
    for i in range(n):
        f = []
        for j in range(n):
            f.append(" ")
 
        M.append(f)
 
    return M
 
# pinta_dau() pinta el núnmero que se li passi en un dau de dimensions n X n
def pinta_dau(n,numero):
 
    d = construeix_dau(n)
 
    if numero == 1:
        d[n//2][n//2] = "o"        
 
    if numero == 2:
        d[0][0] = "o"        
        d[n-1][n-1] = "o"
 
    if numero == 3:
        d[0][0] = "o"        
        d[n//2][n//2] = "o"        
        d[n-1][n-1] = "o"
 
    if numero == 4:
<<<<<<< HEAD
        d[0][0] = "o"        
        d[n-1][0] = "o"
        d[0][n-1] = "o"        
        d[n-1][n-1] = "o"
 
    if numero == 5:    
        d[0][0] = "o"
=======
        d[0][0] = "o"
        d[0][n-1] = "o"
        d[n-1][0] = "o"
        d[n-1][n-1] = "o"


    if numero == 5:
        d[0][0] = "o" 
>>>>>>> 7b93c5715e089d316b4305719018bc00ca30f6c4
        d[0][n-1] = "o"
        d[n//2][n//2] = "o"
        d[n-1][0] = "o"
        d[n-1][n-1] = "o"
 
    if numero == 6:
        d[0][0] = "o"        
        d[n-1][0] = "o"
        d[0][n-1] = "o"        
        d[n-1][n-1] = "o"
        d[n//2][0] = "o"        
        d[n//2][n-1] = "o"        
 
    return d
 
 
def escriu_dau(d):
    n = len(d)
    for i in range(n):
        print(d[i])
 
 
 
def tirar_dau():
    numero = randint(1,6)
    dau = pinta_dau(3,numero)
<<<<<<< HEAD
    escriu_dau(dau)        
=======
    escriu_dau(dau)
>>>>>>> 7b93c5715e089d316b4305719018bc00ca30f6c4
    return numero

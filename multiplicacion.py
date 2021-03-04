def tablamulti():
    numero = int(input("Indica un numero: "))
    for f in range(1, 11, 1):
        multiplicacion = numero * f
        print(str(f) + "*" + str(numero) + "=" + str(multiplicacion))

def main():
    tablamulti()

main()           

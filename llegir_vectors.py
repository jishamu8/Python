#llegir vector
def llegir_vector():
    n = llegir_dimensio()
    v = llegir_contingut(n)

    return v


def llegir_dimensio():
    print("Dimensio del vector? ")
    n = int(input())

    return n


def llegir_contingut(n):
    v = []
    for i in range(n):
        print("Entra la component numero " + str(i+1) + ":")
        x = int(input())
        v.append(x)

    return v

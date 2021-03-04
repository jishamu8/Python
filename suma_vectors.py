from llegir_vectors import llegir_dimensio
from llegir_vectors import llegir_contingut

def suma_vectors():
    n = llegir_dimensio()
    print("Primer vector")
    v1= llegir_contingut(n)
    print("Segon vector")
    v2 = llegir_contingut(n)
    v = []
    for i in range (n):
        s = v1[i] + v2[i]
        v.append(s)

    return v
